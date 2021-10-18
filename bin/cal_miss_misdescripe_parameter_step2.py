#*-*coding=utf-8*-*
import os
import xml.dom.minidom
import sys
sys.path.append('.')
import calInterArea
import codecs
#detection_result_path = './results/'
ground_truth_path = '/home/igi/media/czf/LJJJ_Fittings/val_step2/labels/'
#这个路径是什么
draw_path='./special_pic'
import shutil,argparse

def calParameter(threshHold,detection_result_path,class_num):
    allfile_res = []
    #这个是小区域的类别,要按照preproc里的顺序写
    # useful_tag= ["37_NZXJ_YJSX","38_XXXJ","41_NZXJ","44_NZXJ_YYX","NZXJ_yjh",
    #     "NZXJ_yjb","XCXJ1","XCXJ2","XCXJ3",
    #     "QTJJ","4_Socket Clevis_W&WS","6_Bolt_U&UJ",
    #     "ZJGB_1","ZJGB_2","ZJGB_3","Yoke_Plate"]
    useful_tag= [class_num]
    tag_dir={0:"37_NZXJ_YJSX",1:"38_XXXJ",2:"41_NZXJ",3:"44_NZXJ_YYX",4:"NZXJ_yjh",
        5:"NZXJ_yjb",6:"XCXJ1",7:"XCXJ2",8:"XCXJ3",
        9:"QTJJ",10:"4_Socket Clevis_W&WS",11:"6_Bolt_U&UJ",
        12:"ZJGB_1",13:"ZJGB_2",14:"ZJGB_3",15:"Yoke_Plate"}
    # useful_tag=['XCXJ_XS']
    #大区域
    # useful_tag=['XCXJ_JJC','44_NZXJ_YYX','41_NZXJ']

    #这两个文件是干什么的
    # if not os.path.isdir("./misinformation"):
    #     os.makedirs("./misinformation")
    # if not os.path.isdir("./leak_detection"):
    #     os.makedirs("./leak_detection")
    detection_file_list = os.listdir(detection_result_path)
    for i in range(len(detection_file_list)):

        ground_truth_file = ground_truth_path + detection_file_list[i]
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

                if not int(tmplist[0]) in useful_tag:
                    continue

                label_des_detection['name'] = tmplist[0]  # useful_tag[0]#
                label_des_detection['xmin'] = str(tmplist[2])
                label_des_detection['xmax'] = str(tmplist[3])
                label_des_detection['ymin'] = str(tmplist[4])
                label_des_detection['ymax'] = str(tmplist[5])
                label_des_detection['match'] = "False"
                label_des_detection['file_dir'] = ground_truth_file
                res['detection_result'].append(label_des_detection)
            #打开真实label
            f = codecs.open(os.path.join(ground_truth_path ,detection_file_list[i]), 'r', encoding='utf-8')
            label_list = f.readlines()

            for _j in range(1,len(label_list)):
                tmplist2 = label_list[_j].strip().split(' ')

                label_des_xml = {
                    "name": "",
                    "xmin": "",
                    "ymin": "",
                    "xmax": "",
                    "ymax": "",
                    "match": "",
                    "file_dir": ""
                }
                #真实lable
                name = tmplist2[0]

                if not int(name) in useful_tag:
                    continue

                label_des_xml['name'] = name  # useful_tag[0]
                label_des_xml['xmin'] = str(tmplist2[1])
                label_des_xml['xmax'] = str(tmplist2[2])
                label_des_xml['ymin'] = str(tmplist2[3])
                label_des_xml['ymax'] = str(tmplist2[4])
                label_des_xml['match'] = "False"
                label_des_xml["file_dir"] = ground_truth_file
                res['ground_truth'].append(label_des_xml)
            allfile_res.append(res)
        else:
            print('{} is not exist!'.format(ground_truth_file))
    #进行匹配
    match_file_list = []
    for result in allfile_res:
        # print(result["detection_result"])
        # print(result["ground_truth"])
        # print('-'*20)
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
    print("类别：{}，置信度：{}".format(tag_dir[class_num],threshHold))
    print("漏检率是:{}".format((all_bz_num - detect_bz_num) / float(all_bz_num + 0.0000001)))
    print("误报率是:{}".format((all_predict_num - detect_predict_num) / float(all_predict_num + 0.0000001)))
    #lj =(all_bz_num - detect_bz_num) / float(all_bz_num + 0.0000001)
    #print("length is {}".format(len(match_file_list)))
    return (all_bz_num - detect_bz_num) / float(all_bz_num + 0.0000001),(all_predict_num - detect_predict_num) / float(all_predict_num + 0.0000001)
    # for line_file in match_file_list:
    #     print(line_file)
# from tqdm import tqdm
if __name__=="__main__":
    #lj, wb = calParameter(0.76)
    argparser = argparse.ArgumentParser(description='test phase')
    argparser.add_argument('-r', type=str, default='')
    args = argparser.parse_args()
    detection_result_path = '/home/igi/media/czf/LJJJ_Fittings/val_step2/model_out'
    res = []
    # pbar=tqdm(range(50))
    # txt_write = codecs.open('/home/igi/media/yhy/jinjuxiushi/test_dataset/' + 'writer'+'.txt', 'w', encoding='utf-8')
    for i in range(16):
        print('='*20)
        for thres in range(20,91,10):
            #thres是置信度
            thres=float(thres/100.0)
            lj,wb=calParameter(thres,detection_result_path,i)
            res.append([thres,lj,wb])





