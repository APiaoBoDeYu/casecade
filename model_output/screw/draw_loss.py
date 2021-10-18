#coding=utf-8
import os, re, traceback
import matplotlib.pyplot as plt
class LogVisual:

    it=1
    def readFile(self, path):
        file = open(path, 'r')
        lines = [line.strip() for line in file.readlines()]
        #print(lines)
        file.close()
        return lines
    def parse_iter(self, id, iter_lines):
        # if len(iter_lines) != 6:
        #     pass
        global epoch_tem
        try:
            epoch,s2_loss_cls, s0_loss_bbox, loss_rpn_bbox, loss_rpn_cls, s1_acc, s0_acc, s1_loss_bbox, s1_loss_cls,s0_loss_cls,s2_loss_bbox,s2_acc,loss = None,None, None, None, None, None, None,None, None, None, None, None,None
            for line in iter_lines:
                line1=line.split(',')
                if len(line1)!=1:
                    if 'day' in line1[2]:
                        diff = 0
                    else:
                        diff = -1
                    iter=int(id)
                    #获取epoch
                    epoch_num=line1[1].find('Epoch [')

                    epoch =float(line1[1][epoch_num+7:epoch_num+8])
                    if epoch==9:
                        epoch_tem=9
                    if epoch<epoch_tem:
                        epoch = float(line1[1][epoch_num + 7:epoch_num + 9])
                        epoch_tem=epoch

                    s2_loss_cls=float(line1[7+diff][-6:])
                    s0_loss_bbox=float(line1[8+diff][-6:])
                    loss_rpn_bbox=float(line1[9+diff][-6:])
                    loss_rpn_cls=float(line1[10+diff][-6:])
                    s1_acc=float(line1[11+diff][-7:])
                    s0_acc=float(line1[12+diff][-7:])
                    s1_loss_bbox=float(line1[13+diff][-6:])
                    s1_loss_cls=float(line1[14+diff][-6:])
                    s0_loss_cls=float(line1[15+diff][-6:])
                    s2_loss_bbox=float(line1[16+diff][-6:])
                    s2_acc=float(line1[17+diff][-7:])
                    loss=float(line1[18+diff][-6:])

                else:
                    continue
            return (epoch,iter, s2_loss_cls, s0_loss_bbox, loss_rpn_bbox, loss_rpn_cls, s1_acc, s0_acc, s1_loss_bbox, s1_loss_cls,s0_loss_cls,s2_loss_bbox,s2_acc,loss)
        except Exception as err:
            traceback.print_exc()
        return None
    def draw_loss(self):
        pass
    def parse_log(self,log_path,skip_num=25000):
        lines = self.readFile(log_path)
        iter_ress = []
        iter_lines = []
        for idx,line in enumerate(lines[2:]):
            # if 'epoch' in line and 'iter'in line:
                #print(line)
                iter_lines.append(line)

            #if 'Iteration' in line and ' sgd_solver.cpp' in line:
            #if 'epoch' in line:
                #print (iter_lines)
                # print ('####')
                iter_res = self.parse_iter(idx,iter_lines)
                #print (iter_res)
                if  iter_res is None :
                    #print ('1')
                    a=[]
                else:
                    iter_ress.append(iter_res)
                    iter_lines = []
        #print (iter_lines)
        # for idx,elem in enumerate(iter_ress):
        #     print(elem[1])
        # epoch, iter, s2_loss_cls, s0_loss_bbox, loss_rpn_bbox, loss_rpn_cls, s1_acc, s0_acc, s1_loss_bbox, s1_loss_cls, s0_loss_cls, s2_loss_bbox, s2_acc, loss
        epoch=[elem[0] for idx,elem in enumerate(iter_ress) if idx%42==0]
        iter= [elem[1] for idx,elem in enumerate(iter_ress) if idx%42==0]
        s2_loss_cls = [elem[2] for idx,elem in enumerate(iter_ress) if idx%42==0]
        s0_loss_bbox = [elem[3] for idx,elem in enumerate(iter_ress) if idx%42==0 ]
        loss_rpn_bbox = [elem[4] for idx,elem in enumerate(iter_ress) if idx%42==0 ]
        loss_rpn_cls = [elem[5] for idx,elem in enumerate(iter_ress) if idx%42==0 ]
        s1_acc = [elem[6] for idx,elem in enumerate(iter_ress) if idx%42==0 ]
        s0_acc = [elem[7] for idx,elem in enumerate(iter_ress) if idx%42==0 ]
        s1_loss_bbox = [elem[8] for idx,elem in enumerate(iter_ress) if idx%42==0 ]
        s1_loss_cls = [elem[9] for idx,elem in enumerate(iter_ress) if idx%42==0 ]
        s0_loss_cls = [elem[10] for idx,elem in enumerate(iter_ress) if idx%42==0 ]
        s2_loss_bbox = [elem[11] for idx,elem in enumerate(iter_ress) if idx%42==0 ]
        s2_acc = [elem[12] for idx,elem in enumerate(iter_ress) if idx%42==0 ]
        loss = [elem[13] for idx,elem in enumerate(iter_ress) if idx%42==0 ]
        print (iter)
        plt.subplot(511)
        plt.title('s2_loss_cls')
        plt.plot(epoch, s2_loss_cls, c='green')
        plt.subplot(512)
        plt.title('s0_loss_bbox')
        plt.plot(epoch, s0_loss_bbox, c='green')
        plt.subplot(513)
        plt.title('loss_rpn_bbox')
        plt.plot(epoch, loss_rpn_bbox, c='green')
        plt.subplot(514)
        plt.title('loss_rpn_cls')
        plt.plot(epoch, loss_rpn_cls, c='green')
        plt.subplot(515)
        plt.title('loss')
        plt.plot(epoch,loss, c='green')
        plt.savefig("./loss1.jpg")
        plt.show()

        plt.subplot(411)
        plt.title('s1_loss_bbox')
        plt.plot(epoch,s1_loss_bbox, c='green')
        plt.subplot(412)
        plt.title('s1_loss_cls')
        plt.plot(epoch,s1_loss_cls, c='green')
        plt.subplot(413)
        plt.title('s0_loss_cls')
        plt.plot(epoch,s0_loss_cls, c='green')
        plt.subplot(414)
        plt.title('s2_loss_bbox')
        plt.plot(epoch,s2_loss_bbox, c='green')
        plt.savefig("./loss2.jpg")
        plt.show()

        plt.subplot(311)
        plt.title('s1_acc')
        plt.plot(epoch,s1_acc, c='green')
        plt.subplot(312)
        plt.title('s0_acc')
        plt.plot(epoch,s0_acc, c='green')
        plt.subplot(313)
        plt.title('s2_acc')
        plt.plot(epoch,s2_acc, c='green')
        plt.savefig("./acc.jpg")
        plt.show()
if __name__ == '__main__':
    epoch_tem=0
    logVisual = LogVisual()
    log_path = r'./20210802_105104.log'
    logVisual.parse_log(log_path)
