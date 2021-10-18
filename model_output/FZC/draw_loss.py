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

        try:
            iter, tot_loss, loss_box, loss_cls, rpn_loss_cls, rpn_loss_box = None, None, None, None, None, None
            for line in iter_lines:
                line1=line.split(',')

                if len(line1)!=1:
                    # a=line1[0].split(' ')
                    # iter=a[1]
                    iter=int(id)
                    #print(iter)
                    #print (a,iter)
                    tot_loss=float(line1[5][-6:])
                    loss_box=float(line1[4][-6:])
                    loss_cls=float(line1[3][-6:])
                    rpn_loss_cls=float(line1[1][-6:])
                    rpn_loss_box=float(line1[2][-6:])
                else:
                    continue
            return (iter, tot_loss, loss_box, loss_cls, rpn_loss_cls, rpn_loss_box)
        except Exception as err:
            traceback.print_exc()
        return None
    def draw_loss(self):
        pass
    def parse_log(self,log_path,skip_num=25000):
        lines = self.readFile(log_path)
        iter_ress = []
        iter_lines = []
        for idx,line in enumerate(lines[3000:]):
            # print(idx)
            # print ("############")
            #print (line)
            #line1=line.split(',')
            #print(line1)
            if 'epoch' in line and 'iter'in line:
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
        iter= [elem[0] for idx,elem in enumerate(iter_ress) if idx%100==0]
        tot_loss = [elem[1] for idx,elem in enumerate(iter_ress) if idx%100==0]
        loss_box = [elem[2] for idx,elem in enumerate(iter_ress) if idx%100==0 ]
        loss_cls = [elem[3] for idx,elem in enumerate(iter_ress) if idx%100==0 ]
        rpn_loss_cls = [elem[4] for idx,elem in enumerate(iter_ress) if idx%100==0 ]
        rpn_loss_box = [elem[5] for idx,elem in enumerate(iter_ress) if idx%100==0 ]
        print (iter)
        plt.subplot(511)
        plt.title('tot_loss')
        plt.plot(iter, tot_loss, c='green')
        plt.subplot(512)
        plt.title('loss_box')
        plt.plot(iter, loss_box, c='green')
        plt.subplot(513)
        plt.title('loss_cls')
        plt.plot(iter, loss_cls, c='green')
        plt.subplot(514)
        plt.title('rpn_loss_cls')
        plt.plot(iter, rpn_loss_cls, c='green')
        plt.subplot(515)
        plt.title('rpn_loss_box')
        plt.plot(iter,rpn_loss_box, c='green')
        plt.show()
if __name__ == '__main__':
    logVisual = LogVisual()
    log_path = r'/home/igi/media/yhy/casecade/model_output/FZC/train_logs.txt'
    logVisual.parse_log(log_path)
