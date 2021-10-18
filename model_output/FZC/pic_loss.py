import matplotlib.pyplot as plt
# with open('train_logs.txt') as f:
#     lines = f.readlines()
#     desired_lines = lines[5:]
#     Xtemp = []
#     x = []
#     Ytemp=[]
#     y = []
#     epoch = -1
#     for i in desired_lines:
#         i = i.strip('\n')
#         num = i.find('tot_losses: ')
#         if len(i) != 0 and num != -1:
#             value = i[num + 12:num + 18]
#             value = float(value)
#             Xtemp.append(epoch)
#             Ytemp.append(value)
#         else:
#             epoch += 1
#             x.append(Xtemp[-1])
#             y.append(Ytemp[-1])
# plt.plot(x, y)
# plt.xlabel("Epoch")
# plt.ylabel("loss")
# plt.savefig("./loss.jpg")
# plt.show()

# 需要记录的变量
# s0.loss_bbox:
# s1.loss_bbox:
# s2.loss_bbox:
# loss_rpn_bbox:
# loss_rpn_cls:
# s0.acc:
# s1.acc:
# s2.acc:
# s0.loss_cls:
# s1.loss_cls:
# s2.loss_cls:
# loss:

def plt_loss():
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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
    with open('./../region/20210729_113846.log') as f:
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



if __name__ == "__main__":
    plt_loss()
    plt_s0_acc()
    plt_s1_acc()
    plt_s2_acc()
    plt_s0_loss_cls()
    plt_s1_loss_cls()
    plt_s2_loss_cls()
    s0_loss_bbox()
    s1_loss_bbox()
    s2_loss_bbox()
    loss_rpn_bbox()
    loss_rpn_cls()

    # plt_loss_all()
    # plt_s0_acc_all()