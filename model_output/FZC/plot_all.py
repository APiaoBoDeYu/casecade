import matplotlib.pyplot as plt
import traceback

log_file='20210914_094124.log'
def plt_loss():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for i in desired_lines:
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('loss: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                epoch=float(epoch)
                value = i[num + 6:num + 12]
                value = float(value)
                Xtemp.append(epoch)
                Ytemp.append(value)
                if temp<epoch:
                    x.append(Xtemp[-1])
                    y.append(Ytemp[-1])
                    temp=epoch
        plt.plot(x, y)
        plt.xlabel("Epoch")
        plt.ylabel("loss")
        plt.savefig("./loss.jpg")
        plt.show()

def plt_loss_all():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for e_i,i in enumerate(desired_lines):
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('loss: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                # epoch=float(epoch)
                x_label=str(epoch)+'_'+str(e_i)
                value = i[num + 6:num + 12]
                value = float(value)
                Xtemp.append(x_label)
                Ytemp.append(value)
                if temp<int(epoch):
                #     x.append(Xtemp[-1])
                #     y.append(Ytemp[-1])
                    temp=int(epoch)
        plt.plot(Xtemp, Ytemp)
        plt.xlabel("Epoch")
        plt.ylabel("loss")
        plt.savefig("./loss.jpg")
        plt.show()

## s0.acc:
def plt_s0_acc():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for i in desired_lines:
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('s0.acc: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                epoch=float(epoch)
                value = i[num + 8:num + 15]
                value = float(value)
                Xtemp.append(epoch)
                Ytemp.append(value)
                if temp<epoch:
                    x.append(Xtemp[-1])
                    y.append(Ytemp[-1])
                    temp=epoch
        plt.plot(x, y)
        plt.xlabel("Epoch")
        plt.ylabel("s0_acc")
        plt.savefig("./s0_acc.jpg")
        plt.show()

def plt_s0_acc_all():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0
        #
        # for i in desired_lines:
        #     i = i.strip('\n')
        #     epoch_num=i.find('Epoch [')
        #     num = i.find('s0.acc: ')
        #     if len(i) != 0 and num != -1:
        #         epoch=i[epoch_num+7:epoch_num+8]
        #         if float(epoch)<temp:
        #             epoch = i[epoch_num + 7:epoch_num + 9]
        #         epoch=float(epoch)
        #         value = i[num + 8:num + 15]
        #         value = float(value)
        #         Xtemp.append(epoch)
        #         Ytemp.append(value)
        #         if temp<epoch:
        #             x.append(Xtemp[-1])
        #             y.append(Ytemp[-1])
        #             temp=epoch
        # plt.plot(x, y)

        for e_i,i in enumerate(desired_lines):
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('s0.acc: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                # epoch=float(epoch)
                x_label=str(epoch)+'_'+str(e_i)
                value = i[num + 8:num + 15]
                value = float(value)
                Xtemp.append(x_label)
                Ytemp.append(value)
                if temp<int(epoch):
                #     x.append(Xtemp[-1])
                #     y.append(Ytemp[-1])
                    temp=int(epoch)
        plt.plot(Xtemp, Ytemp)
        plt.xlabel("Epoch")
        plt.ylabel("s0_acc")
        plt.savefig("./s0_acc.jpg")
        plt.show()

#s1.acc
def plt_s1_acc():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for i in desired_lines:
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('s1.acc: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                epoch=float(epoch)
                value = i[num + 8:num + 15]
                value = float(value)
                Xtemp.append(epoch)
                Ytemp.append(value)
                if temp<epoch:
                    x.append(Xtemp[-1])
                    y.append(Ytemp[-1])
                    temp=epoch
        plt.plot(x, y)
        plt.xlabel("Epoch")
        plt.ylabel("s1_acc")
        plt.savefig("./s1_acc.jpg")
        plt.show()

#s2.acc
def plt_s2_acc():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for i in desired_lines:
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('s2.acc: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                epoch=float(epoch)
                value = i[num + 8:num + 15]
                value = float(value)
                Xtemp.append(epoch)
                Ytemp.append(value)
                if temp<epoch:
                    x.append(Xtemp[-1])
                    y.append(Ytemp[-1])
                    temp=epoch
        plt.plot(x, y)
        plt.xlabel("Epoch")
        plt.ylabel("s2_acc")
        plt.savefig("./s2_acc.jpg")
        plt.show()

# s0.loss_cls:
def plt_s0_loss_cls():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for i in desired_lines:
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('s0.loss_cls: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                epoch=float(epoch)
                value = i[num + 13:num + 19]
                value = float(value)
                Xtemp.append(epoch)
                Ytemp.append(value)
                if temp<epoch:
                    x.append(Xtemp[-1])
                    y.append(Ytemp[-1])
                    temp=epoch
        plt.plot(x, y)
        plt.xlabel("Epoch")
        plt.ylabel("s0_loss_cls")
        plt.savefig("./s0_loss_cls.jpg")
        plt.show()

# s1.loss_cls:
def plt_s1_loss_cls():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for i in desired_lines:
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('s1.loss_cls: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                epoch=float(epoch)
                value = i[num + 13:num + 19]
                value = float(value)
                Xtemp.append(epoch)
                Ytemp.append(value)
                if temp<epoch:
                    x.append(Xtemp[-1])
                    y.append(Ytemp[-1])
                    temp=epoch
        plt.plot(x, y)
        plt.xlabel("Epoch")
        plt.ylabel("s1_loss_cls")
        plt.savefig("./s1_loss_cls.jpg")
        plt.show()

# s2.loss_cls:
def plt_s2_loss_cls():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for i in desired_lines:
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('s2.loss_cls: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                epoch=float(epoch)
                value = i[num + 13:num + 19]
                value = float(value)
                Xtemp.append(epoch)
                Ytemp.append(value)
                if temp<epoch:
                    x.append(Xtemp[-1])
                    y.append(Ytemp[-1])
                    temp=epoch
        plt.plot(x, y)
        plt.xlabel("Epoch")
        plt.ylabel("s2_loss_cls")
        plt.savefig("./s2_loss_cls.jpg")
        plt.show()

# s0.loss_bbox:
def s0_loss_bbox():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for i in desired_lines:
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('s0.loss_bbox: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                epoch=float(epoch)
                value = i[num + 14:num + 20]
                value = float(value)
                Xtemp.append(epoch)
                Ytemp.append(value)
                if temp<epoch:
                    x.append(Xtemp[-1])
                    y.append(Ytemp[-1])
                    temp=epoch
        plt.plot(x, y)
        plt.xlabel("Epoch")
        plt.ylabel("s0_loss_bbox")
        plt.savefig("./s0_loss_bbox.jpg")
        plt.show()

# s1.loss_bbox:
def s1_loss_bbox():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for i in desired_lines:
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('s1.loss_bbox: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                epoch=float(epoch)
                value = i[num + 14:num + 20]
                value = float(value)
                Xtemp.append(epoch)
                Ytemp.append(value)
                if temp<epoch:
                    x.append(Xtemp[-1])
                    y.append(Ytemp[-1])
                    temp=epoch
        plt.plot(x, y)
        plt.xlabel("Epoch")
        plt.ylabel("s1_loss_bbox")
        plt.savefig("./s1_loss_bbox.jpg")
        plt.show()
# s2.loss_bbox:
def s2_loss_bbox():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for i in desired_lines:
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('s2.loss_bbox: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                epoch=float(epoch)
                value = i[num + 14:num + 20]
                value = float(value)
                Xtemp.append(epoch)
                Ytemp.append(value)
                if temp<epoch:
                    x.append(Xtemp[-1])
                    y.append(Ytemp[-1])
                    temp=epoch
        plt.plot(x, y)
        plt.xlabel("Epoch")
        plt.ylabel("s2_loss_bbox")
        plt.savefig("./s2_loss_bbox.jpg")
        plt.show()
# loss_rpn_bbox:
def loss_rpn_bbox():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for i in desired_lines:
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('loss_rpn_bbox: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                epoch=float(epoch)
                value = i[num + 15:num + 21]
                value = float(value)
                Xtemp.append(epoch)
                Ytemp.append(value)
                if temp<epoch:
                    x.append(Xtemp[-1])
                    y.append(Ytemp[-1])
                    temp=epoch
        plt.plot(x, y)
        plt.xlabel("Epoch")
        plt.ylabel("loss_rpn_bbox")
        plt.savefig("./loss_rpn_bbox.jpg")
        plt.show()

# loss_rpn_cls:
def loss_rpn_cls():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for i in desired_lines:
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('loss_rpn_cls: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                epoch=float(epoch)
                value = i[num + 14:num + 20]
                value = float(value)
                Xtemp.append(epoch)
                Ytemp.append(value)
                if temp<epoch:
                    x.append(Xtemp[-1])
                    y.append(Ytemp[-1])
                    temp=epoch
        plt.plot(x, y)
        plt.xlabel("Epoch")
        plt.ylabel("loss_rpn_cls")
        plt.savefig("./loss_rpn_cls.jpg")
        plt.show()



def plt_loss_all():
    with open('./../region/%s'%log_file) as f:
        lines = f.readlines()
        desired_lines = lines[2:]
        Xtemp = []
        x = []
        Ytemp=[]
        y = []
        temp = 0

        for e_i,i in enumerate(desired_lines):
            i = i.strip('\n')
            epoch_num=i.find('Epoch [')
            num = i.find('loss: ')
            if len(i) != 0 and num != -1:
                epoch=i[epoch_num+7:epoch_num+8]
                if float(epoch)<temp:
                    epoch = i[epoch_num + 7:epoch_num + 9]
                # epoch=float(epoch)
                x_label=str(epoch)+'_'+str(e_i)
                value = i[num + 6:num + 12]
                value = float(value)
                Xtemp.append(x_label)
                Ytemp.append(value)
                if temp<int(epoch):
                #     x.append(Xtemp[-1])
                #     y.append(Ytemp[-1])
                    temp=int(epoch)
        plt.plot(Xtemp, Ytemp)
        plt.xlabel("Epoch")
        plt.ylabel("loss")
        plt.savefig("./loss.jpg")
        plt.show()


class LogVisual():
    it=1
    def readFile(self, path):
        file = open(path, 'r')
        lines = [line.strip() for line in file.readlines()]
        #print(lines)
        file.close()
        return lines

    def parse_iter(self, id, iter_lines):

        try:
           # s0_loss_bbox: 0_0184,
           #  s2_loss_bbox: 0_0226, s1_acc: 98_2123, loss_rpn_bbox: 0_0020, s0_loss_cls: 0_0428, loss_rpn_cls: 0_0009, s0_acc: 98_3027,
           # s1_loss_cls: 0_0231, s1_loss_bbox: 0_0265, s2_acc: 98_0263, s2_loss_cls: 0_0126, loss: 0_1489

            s0_loss_bbox, s2_loss_bbox, s1_acc, loss_rpn_bbox, s0_loss_cls, loss_rpn_cls = None, None, None, None, None, None
            s0_acc, s1_loss_cls, s1_loss_bbox, s2_acc, s2_loss_cls, loss = None, None, None, None, None, None
            for line in iter_lines:
                line1=line.split(',')

                if 'day' not in line1[2]:
                    line1.insert(3,'useless')

                if len(line1)!=1:
                    epoch_num=line1[1].find('Epoch [')
                    if ord(line1[1][epoch_num+8])==93:
                        epoch = line1[1][epoch_num + 7:epoch_num + 8]
                    else:
                        epoch = line1[1][epoch_num + 7:epoch_num + 9]
                    epoch = int(epoch)

                    iter=int(id)
                    s0_loss_bbox=float(line1[7][-6:])
                    s2_loss_bbox=float(line1[8][-6:])
                    s1_acc=float(line1[9][-7:])
                    loss_rpn_bbox=float(line1[17][-6:])
                    s0_loss_cls=float(line1[11][-6:])
                    loss_rpn_cls=float(line1[12][-6:])
                    s0_acc=float(line1[13][-7:])
                    s1_loss_cls=float(line1[14][-6:])
                    s1_loss_bbox=float(line1[15][-6:])
                    s2_acc=float(line1[16][-7:])
                    s2_loss_cls=float(line1[8][-6:])
                    loss=float(line1[18][-6:])

                else:
                    continue
            return (epoch, iter, s0_loss_bbox, s2_loss_bbox, s1_acc, loss_rpn_bbox, s0_loss_cls, loss_rpn_cls,s0_acc, s1_loss_cls, s1_loss_bbox, s2_acc, s2_loss_cls, loss)
        except Exception as err:
            traceback.print_exc()
        return None

    def parse_iter(self, id, iter_lines):

        try:
           # s0_loss_bbox: 0_0184,
           #  s2_loss_bbox: 0_0226, s1_acc: 98_2123, loss_rpn_bbox: 0_0020, s0_loss_cls: 0_0428, loss_rpn_cls: 0_0009, s0_acc: 98_3027,
           # s1_loss_cls: 0_0231, s1_loss_bbox: 0_0265, s2_acc: 98_0263, s2_loss_cls: 0_0126, loss: 0_1489

            s0_loss_bbox, s2_loss_bbox, s1_acc, loss_rpn_bbox, s0_loss_cls, loss_rpn_cls = None, None, None, None, None, None
            s0_acc, s1_loss_cls, s1_loss_bbox, s2_acc, s2_loss_cls, loss = None, None, None, None, None, None
            for line in iter_lines:
                line1=line.split(',')

                if 'day' not in line1[2]:
                    line1.insert(3,'useless')

                if len(line1)!=1:
                    epoch_num=line1[1].find('Epoch [')
                    if ord(line1[1][epoch_num+8])==93:
                        epoch = line1[1][epoch_num + 7:epoch_num + 8]
                    else:
                        epoch = line1[1][epoch_num + 7:epoch_num + 9]
                    epoch = int(epoch)

                    for i,tex in enumerate(line1):
                        print("%d:\t%s"%(i,tex))

                    # iter=int(id)
                    # s0_loss_bbox=float(line1[7][-6:])
                    # s2_loss_bbox=float(line1[8][-6:])
                    # s1_acc=float(line1[9][-7:])
                    # loss_rpn_bbox=float(line1[10][-6:])
                    # s0_loss_cls=float(line1[11][-6:])
                    # loss_rpn_cls=float(line1[12][-6:])
                    # s0_acc=float(line1[13][-7:])
                    # s1_loss_cls=float(line1[14][-6:])
                    # s1_loss_bbox=float(line1[15][-6:])
                    # s2_acc=float(line1[16][-7:])
                    # s2_loss_cls=float(line1[17][-6:])
                    # loss=float(line1[18][-6:])
                    iter=int(id)
                    s0_loss_bbox=float(line1[9][-6:])
                    s2_loss_bbox=float(line1[7][-6:])
                    s1_acc=float(line1[16][-7:])
                    loss_rpn_bbox=float(line1[17][-6:])
                    s0_loss_cls=float(line1[11][-6:])
                    loss_rpn_cls=float(line1[15][-6:])
                    s0_acc=float(line1[13][-7:])
                    s1_loss_cls=float(line1[14][-6:])
                    s1_loss_bbox=float(line1[12][-6:])
                    s2_acc=float(line1[10][-7:])
                    s2_loss_cls=float(line1[8][-6:])
                    loss=float(line1[18][-6:])

                else:
                    continue
            return (epoch, iter, s0_loss_bbox, s2_loss_bbox, s1_acc, loss_rpn_bbox, s0_loss_cls, loss_rpn_cls,s0_acc, s1_loss_cls, s1_loss_bbox, s2_acc, s2_loss_cls, loss)
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
            if 'Epoch' in line:
                #print(line)
                iter_lines.append(line)
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
        # epoch=[elem[0] for idx,elem in enumerate(iter_ress) if idx%100==0]
        iter= [elem[1] for idx,elem in enumerate(iter_ress) if idx%10==0]

        s0_loss_bbox = [elem[2] for idx,elem in enumerate(iter_ress) if idx%10==0]
        s2_loss_bbox = [elem[3] for idx,elem in enumerate(iter_ress) if idx%10==0]
        s1_acc = [elem[4] for idx,elem in enumerate(iter_ress) if idx%10==0]
        loss_rpn_bbox = [elem[5] for idx,elem in enumerate(iter_ress) if idx%10==0]
        s0_loss_cls = [elem[6] for idx,elem in enumerate(iter_ress) if idx%10==0]
        loss_rpn_cls = [elem[7] for idx,elem in enumerate(iter_ress) if idx%10==0]
        s0_acc = [elem[8] for idx,elem in enumerate(iter_ress) if idx%10==0]
        s1_loss_cls = [elem[9] for idx,elem in enumerate(iter_ress) if idx%10==0]
        s1_loss_bbox = [elem[10] for idx,elem in enumerate(iter_ress) if idx%10==0]
        s2_acc = [elem[11] for idx,elem in enumerate(iter_ress) if idx%10==0]
        s2_loss_cls = [elem[12] for idx,elem in enumerate(iter_ress) if idx%10==0]
        loss = [elem[13] for idx,elem in enumerate(iter_ress) if idx%10==0]

        print (iter)
        plt.figure(figsize=(10, 18))
        plt.subplot(311)
        plt.title('s0_loss_bbox')
        plt.plot(iter, s0_loss_bbox, c='green')
        plt.subplot(312)
        plt.title('s1_loss_bbox')
        plt.plot(iter, s1_loss_bbox, c='green')
        plt.subplot(313)
        plt.title('s2_loss_bbox')
        plt.plot(iter, s2_loss_bbox, c='green')
        plt.savefig("./sx_loss_bbox.jpg")
        # plt.show()

        plt.figure(figsize=(10, 18))
        plt.subplot(311)
        plt.title('s0_loss_cls')
        plt.plot(iter, s0_loss_cls, c='green')
        plt.subplot(312)
        plt.title('s1_loss_cls')
        plt.plot(iter, s1_loss_cls, c='green')
        plt.subplot(313)
        plt.title('s2_loss_cls')
        plt.plot(iter, s2_loss_cls, c='green')
        plt.savefig("./sx_loss_cls.jpg")
        # plt.show()

        plt.figure(figsize=(10, 18))
        plt.subplot(311)
        plt.title('s0_acc')
        plt.plot(iter, s0_acc, c='green')
        plt.subplot(312)
        plt.title('s1_acc')
        plt.plot(iter,s1_acc, c='green')
        plt.subplot(313)
        plt.title('s2_acc')
        plt.plot(iter, s2_acc, c='green')
        plt.savefig("./sx_acc.jpg")
        # plt.show()

        plt.figure(figsize=(10, 18))
        plt.subplot(311)
        plt.title('loss_rpn_bbox')
        plt.plot(iter, loss_rpn_bbox, c='green')
        plt.subplot(312)
        plt.title('loss_rpn_cls')
        plt.plot(iter, loss_rpn_cls, c='green')
        plt.subplot(313)
        plt.title('loss')
        plt.plot(iter, loss, c='green')
        plt.savefig("./loss.jpg")
        # plt.show()

    # def draw_change(self,log_path1,log_path2):
    #     lines1 = self.readFile(log_path1)
    #     lines2 = self.readFile(log_path2)
    #     iter_ress = []
    #     iter_lines = []
    #     # for idx,line1,line2 in enumerate(lines1[2:],lines2[2:]):
    #     #     if 'Epoch' in line2:
    #     #         #print(line)
    #     #         iter_lines.append(line1)
    #     #         iter_res = self.parse_iter(idx,iter_lines)
    #     #         iter_lines=[]
    #     #         iter_lines.append(line2)
    #     #         iter_res = iter_res-self.parse_iter(idx, iter_lines)
    #     #         iter_lines = []
    #     #
    #     #         iter_ress.append(iter_res)
    #
    #     for idx in range(-10,0,1):
    #         x=self.parse_iter(idx,[lines1[idx]])
    #         y=self.parse_iter(idx,[lines2[idx]])
    #         iter_res=list(map(lambda x,y :x-y,self.parse_iter(idx,[lines1[idx]]),self.parse_iter(idx,[lines2[idx]])))
    #         iter_ress.append(iter_res)
    #     # s0.loss_bbox: 0.1011, s2.loss_bbox: 0.0046,
    #     # loss_rpn_bbox: 0.0183, s0.acc: 95.5352, s2.loss_cls: 0.0189,
    #     # loss_rpn_cls: 0.0850, s1.loss_bbox: 0.0311,
    #     # s1.acc: 97.9492, s2.acc: 98.9238, s1.loss_cls: 0.0615, s0.loss_cls: 0.2206, loss: 0.5410
    #     iter= [elem[1] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #
    #     s0_loss_bbox = [elem[2] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #     s2_loss_bbox = [elem[3] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #     s1_acc = [elem[4] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #     loss_rpn_bbox = [elem[5] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #     s0_loss_cls = [elem[6] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #     loss_rpn_cls = [elem[7] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #     s0_acc = [elem[8] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #     s1_loss_cls = [elem[9] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #     s1_loss_bbox = [elem[10] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #     s2_acc = [elem[11] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #     s2_loss_cls = [elem[12] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #     loss = [elem[13] for idx,elem in enumerate(iter_ress) if idx%10==0]
    #
    #     iter =list(range(20))
    #     print (iter)
    #     plt.figure(figsize=(10, 18))
    #     plt.subplot(311)
    #     plt.title('s0_loss_bbox')
    #     plt.plot(iter, s0_loss_bbox, c='green')
    #     plt.subplot(312)
    #     plt.title('s1_loss_bbox')
    #     plt.plot(iter, s1_loss_bbox, c='green')
    #     plt.subplot(313)
    #     plt.title('s2_loss_bbox')
    #     plt.plot(iter, s2_loss_bbox, c='green')
    #     plt.savefig("./sx_loss_bbox.jpg")
    #     plt.show()
    #
    #     plt.figure(figsize=(10, 18))
    #     plt.subplot(311)
    #     plt.title('s0_loss_cls')
    #     plt.plot(iter, s0_loss_cls, c='green')
    #     plt.subplot(312)
    #     plt.title('s1_loss_cls')
    #     plt.plot(iter, s1_loss_cls, c='green')
    #     plt.subplot(313)
    #     plt.title('s2_loss_cls')
    #     plt.plot(iter, s2_loss_cls, c='green')
    #     plt.savefig("./sx_loss_cls.jpg")
    #     plt.show()
    #
    #     plt.figure(figsize=(10, 18))
    #     plt.subplot(311)
    #     plt.title('s0_acc')
    #     plt.plot(iter, s0_acc, c='green')
    #     plt.subplot(312)
    #     plt.title('s1_acc')
    #     plt.plot(iter,s1_acc, c='green')
    #     plt.subplot(313)
    #     plt.title('s2_acc')
    #     plt.plot(iter, s2_acc, c='green')
    #     plt.savefig("./sx_acc.jpg")
    #     plt.show()
    #
    #     plt.figure(figsize=(10, 18))
    #     plt.subplot(311)
    #     plt.title('loss_rpn_bbox')
    #     plt.plot(iter, loss_rpn_bbox, c='green')
    #     plt.subplot(312)
    #     plt.title('loss_rpn_cls')
    #     plt.plot(iter, loss_rpn_cls, c='green')
    #     plt.subplot(313)
    #     plt.title('loss')
    #     plt.plot(iter, loss, c='green')
    #     plt.savefig("./loss.jpg")
    #     plt.show()



if __name__ == "__main__":
    # plt_loss()
    # plt_s0_acc()
    # plt_s1_acc()
    # plt_s2_acc()
    # plt_s0_loss_cls()
    # plt_s1_loss_cls()
    # plt_s2_loss_cls()
    # s0_loss_bbox()
    # s1_loss_bbox()
    # s2_loss_bbox()
    # loss_rpn_bbox()
    # loss_rpn_cls()

    # plt_loss_all()
    # plt_s0_acc_all()
    logVisual = LogVisual()
    log_path = r'/home/igi/media/yhy/casecade/model_output/screw/%s'%log_file
    # log_path1=r'./../region/7_classes/20210729_113846.log'
    logVisual.parse_log(log_path)

    # logVisual.draw_change(log_path1,log_path)