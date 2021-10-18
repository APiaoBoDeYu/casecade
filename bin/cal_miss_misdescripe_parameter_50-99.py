#*-*coding=utf-8*-*
import os
import xml.dom.minidom
import sys
sys.path.append('.')
import calInterArea
import codecs
#detection_result_path = './results/'
ground_truth_path = '/home/igi/media/yhy/jinjuxiushi/test_dataset/xml/'
#这个路径是什么
draw_path='./special_pic'
import shutil,argparse

def calParameter(threshHold,detection_result_path):
    allfile_res = []
    #这个是小区域的类别,要按照preproc里的顺序写
    # useful_tag=['JJXS_yybw','XCXJ_BY3','XCXJ_BY2','NZXJ_yjh','XCXJ_XS']
    # useful_tag=['XCXJ_XS']
    #大区域
    useful_tag=['XCXJ_JJC','44_NZXJ_YYX','41_NZXJ']
    # tag_dir={7:'JJXS_yybw',8:'XCXJ_BY3',9:'XCXJ_BY2',10:'NZXJ_yjh',11:'XCXJ_XS'}
    # tag_dir={11:'XCXJ_XS'}
    #这两个文件是干什么的
    # if not os.path.isdir("./misinformation"):
    #     os.makedirs("./misinformation")
    # if not os.path.isdir("./leak_detection"):
    #     os.makedirs("./leak_detection")
    detection_file_list = os.listdir(detection_result_path)
    for i in range(len(detection_file_list)):
        # print(i)
        ground_truth_file = ground_truth_path + detection_file_list[i][0:-3] + 'xml'
        # print(ground_truth_file)
        res = {"name": "",
               "detection_result": [],
               "ground_truth": []
               }
        if os.path.isfile(ground_truth_file):
            res['name'] = detection_file_list[i][0:-4]
            f = codecs.open(os.path.join(detection_result_path ,detection_file_list[i]), 'r', encoding='utf-8')
            detection_list = f.readlines()
            for _j in range(len(detection_list)):
                #name与match是什么
                label_des_detection = {
                    "name": "",
                    "xmin": "",
                    "ymin": "",
                    "xmax": "",
                    "ymax": "",
                    "match": "",
                    "file_dir": ""
                }
                tmplist = detection_list[_j].strip().split(' ')
                #print(float(tmplist[1]))
                if float(tmplist[1]) < threshHold:#0.95:
                    continue

                if not tmplist[0] in useful_tag:
                    continue
                label_des_detection['name'] = tmplist[0]  # useful_tag[0]#
                label_des_detection['xmin'] = str(tmplist[2])
                label_des_detection['xmax'] = str(tmplist[4])
                label_des_detection['ymin'] = str(tmplist[3])
                label_des_detection['ymax'] = str(tmplist[5])
                label_des_detection['match'] = "False"
                label_des_detection['file_dir'] = ground_truth_file
                res['detection_result'].append(label_des_detection)
            dom = xml.dom.minidom.parse(ground_truth_file)
            #print(ground_truth_file)
            root = dom.documentElement
            labellist = root.getElementsByTagName('object')

            for label in labellist:
                label_des_xml = {
                    "name": "",
                    "xmin": "",
                    "ymin": "",
                    "xmax": "",
                    "ymax": "",
                    "match": "",
                    "file_dir": ""
                }

                name = str(label.getElementsByTagName('name')[0].firstChild.data)
                #print(name)
                if not name in useful_tag:
                    continue
                label_des_xml['name'] = name  # useful_tag[0]
                label_des_xml['xmin'] = str(int(label.getElementsByTagName('xmin')[0].firstChild.data))
                label_des_xml['xmax'] = str(int(label.getElementsByTagName('xmax')[0].firstChild.data))
                label_des_xml['ymin'] = str(int(label.getElementsByTagName('ymin')[0].firstChild.data))
                label_des_xml['ymax'] = str(int(label.getElementsByTagName('ymax')[0].firstChild.data))
                label_des_xml['match'] = "False"
                label_des_xml["file_dir"] = ground_truth_file
                res['ground_truth'].append(label_des_xml)
            allfile_res.append(res)
        else:
            print('{} is not exist!'.format(ground_truth_file))
    match_file_list = []
    for result in allfile_res:
        # print(result["detection_result"])
        # print('\n')
        for detection_item in result["detection_result"]:
            # print(ground_item)

            box1 = (int(detection_item['xmin']), int(detection_item['ymin']),
                    int(detection_item['xmax']), int(detection_item['ymax']))
            for ground_item in result["ground_truth"]:

                box2 = (int(ground_item['xmin']), int(ground_item['ymin']),
                        int(ground_item['xmax']), int(ground_item['ymax']))
                isCheck = calInterArea.solve_coincide(box1, box2)
                isCheck2 = calInterArea.solve_coincide(box2, box1)
                # print(isCheck)
                if isCheck == True or isCheck2 == True:
                    detection_item['match'] = 'True'
                    ground_item['match'] = 'True'

    all_bz_num = 0
    detect_bz_num = 0
    all_predict_num = 0
    detect_predict_num = 0
    # f=open('./tmp.txt','w')
    for result in allfile_res:
        for ground_it in result["ground_truth"]:
            all_bz_num += 1
            if ground_it['match'] == 'True':
                detect_bz_num += 1
            else:
                if not ground_it['file_dir'] in match_file_list:
                    match_file_list.append(ground_it['file_dir'])
                    # shutil.copy('./photo/' +ground_it['file_dir'].split('/')[-1].split('.')[0] + '.jpg' ,
                    #             './leak_detection/' +ground_it['file_dir'].split('/')[-1].split('.')[0] + '.jpg')
                    # f.write('{} {} {} {}\n'.format(ground_it['xmin'],ground_it['ymin'],ground_it['xmax'],ground_it['ymax']))

        for detection_it in result["detection_result"]:
            all_predict_num += 1
            if detection_it['match'] == 'True':
                detect_predict_num += 1
            else:
                if not detection_it['file_dir'] in match_file_list:
                    match_file_list.append(detection_it['file_dir'])
                    # shutil.copy('./photo/' +detection_it['file_dir'].split('/')[-1].split('.')[0] + '.jpg' ,
                    #             './misinformation/' +detection_it['file_dir'].split('/')[-1].split('.')[0] + '.jpg')
            #print(detection_it)
    #print(all_bz_num, detect_bz_num, all_predict_num, detect_predict_num)
    print("\n漏检率是:{}".format((all_bz_num - detect_bz_num) / float(all_bz_num + 0.0000001)))
    print("误报率是:{}".format((all_predict_num - detect_predict_num) / float(all_predict_num + 0.0000001)))
    #lj =(all_bz_num - detect_bz_num) / float(all_bz_num + 0.0000001)
    #print("length is {}".format(len(match_file_list)))
    return (all_bz_num - detect_bz_num) / float(all_bz_num + 0.0000001),(all_predict_num - detect_predict_num) / float(all_predict_num + 0.0000001)
    # for line_file in match_file_list:
    #     print(line_file)
from tqdm import tqdm
if __name__=="__main__":
    #lj, wb = calParameter(0.76)
    argparser = argparse.ArgumentParser(description='test phase')
    argparser.add_argument('-r', type=str, default='')
    args = argparser.parse_args()
    detection_result_path = '/home/igi/media/yhy/jinjuxiushi/test_dataset/results'
    res = []
    pbar=tqdm(range(50)) 
    txt_write = codecs.open('/home/igi/media/yhy/jinjuxiushi/test_dataset/' + 'writer'+'.txt', 'w', encoding='utf-8')
    for thres in range(90,99):
        #thres是置信度
        thres=float(thres/100.0)
        lj,wb=calParameter(thres,detection_result_path)
        pbar.update(1)
        res.append([thres,lj,wb])
    for context in res:
        print("%s,%s,%s"%(context[0],context[1],context[2]))
        txt_write.write("%s,%s,%s\n"%(context[0],context[1],context[2]))




