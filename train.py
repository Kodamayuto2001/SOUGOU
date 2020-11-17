# ニューラルネットワーク２つ
import nn as NN 
# データローダー
import loader as L 

import torch 
import torch.nn.functional as F 
import matplotlib.pyplot as plt 
from tqdm import tqdm
import os 
import cv2 
import numpy as np
import torchvision.transforms as transforms

def test(testDir,label,imgSize,model):
    correct = 0
    
    for cnt,f in enumerate(os.listdir(testDir)):
        # 画像を読み込み
        img = cv2.imread(testDir+"/"+f)
        #print(f)
        #print(cnt)
        #cv2.imshow("img",img)
        # cv2.waitKey(100)

        # チャンネル数を１
        imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # リサイズ
        img = cv2.resize(imgGray,(imgSize,imgSize))

        # リシェイプ
        img = np.reshape(img,(1,imgSize,imgSize))

        # transpose h,c,w
        img = np.transpose(img,(1,2,0))

        # ToTensor 正規化される
        img = img.astype(np.uint8)
        mInput = transforms.ToTensor()(img) 
        mInput = mInput.view(-1, imgSize*imgSize)

        # 推論
        output = model(mInput)
        p = model.forward(mInput)
        if p.argmax() == label:
            correct += 1

        # 推論は1人200枚
        if cnt >= 199:
            break
    
    if label == 0:
        print("Ando    accuracy : {} %".format(100*correct/200))
        return 100*correct/200
    if label == 1:
        print("Higashi accuracy : {} %".format(100*correct/200))
        return 100*correct/200
    if label == 2:
        print("Kataoka accuracy : {} %".format(100*correct/200))
        return 100*correct/200
    if label == 3:
        print("Kodama  accuracy : {} %".format(100*correct/200))
        return 100*correct/200
    if label == 4:
        print("Masuda  accuracy : {} %".format(100*correct/200))
        return 100*correct/200
    if label == 5:
        print("Suetomo accuracy : {} %".format(100*correct/200))
        return 100*correct/200

if __name__ == "__main__":
    ######------hyperParam-----#####
    epoch       = 40
    imgSize     = 160
    Neuron      = 320
    lr          = 0.000005

    batchSize   = 1
    ptName      = "models/nn1.pt"
    lossPng     = "lossImg/loss1.png"
    accPng      = "accImg/acc1.png"
    
    ######------モデルの設定(損失関数も変える)-----#####
    model       = NN.Net_log_softmax(num=6,inputSize=imgSize,Neuron=Neuron)
    # model2      = NN.Net_return_x(num=6,inputSize=imgSize,Neuron=Neuron)

    optimizer   = torch.optim.Adam(params=model.parameters(),lr=lr)

    ######------個別推論用ディレクトリ設定-----#####
    andoDir     = "../ReadOnlyDataSet2/Resources/test/ando"
    higashiDir  = "../ReadOnlyDataSet2/Resources/test/higashi"
    kataokaDir  = "../ReadOnlyDataSet2/Resources/test/kataoka"
    kodamaDir   = "../ReadOnlyDataSet2/Resources/test/kodama"
    masudaDir   = "../ReadOnlyDataSet2/Resources/test/masuda"
    suetomoDir  = "../ReadOnlyDataSet2/Resources/test/suetomo"

    ######------学習用ディレクトリ設定-----#####
    dirImgPath  = dirImgPath = "../ReadOnlyDataSet2/Resources"

    # 学習結果保存用
    R = {
        "trainLoss":[],
        "testLoss":[],
        "testAcc":[],}
    A = {
        "ando":[],
        "higashi":[],
        "kataoka":[],
        "kodama":[],
        "masuda":[],
        "suetomo":[],}



    DL = L.MyDataLoader(trainRootDir=dirImgPath+"/train/",testRootDir=dirImgPath+"/test/",imgSize=imgSize,batchSize=batchSize,num_workers=0)
    loader = DL.getDataLoaders()

    for e in range(epoch):
        for data in tqdm(loader["train"]):
            inputs,label = data 
            optimizer.zero_grad()
            output = model(inputs)
            ######------損失関数-----#####
            loss = F.nll_loss(output,label)
            
            loss.backward()
            optimizer.step()
        R["trainLoss"].append(loss)

        # 学習停止
        model.eval()
        testLoss = 0
        total = 0
        correct = 0
        andoAcc = 0
        higashiAcc = 0
        kataokaAcc = 0
        kodamaAcc = 0
        masudaAcc = 0
        suetomoAcc = 0

        with torch.no_grad():
            andoAcc    = test(andoDir,label=0,imgSize=imgSize,model=model)
            higashiAcc = test(higashiDir,label=1,imgSize=imgSize,model=model)
            kataokaAcc = test(kataokaDir,label=2,imgSize=imgSize,model=model)
            kodamaAcc  = test(kodamaDir,label=3,imgSize=imgSize,model=model)
            masudaAcc  = test(masudaDir,label=4,imgSize=imgSize,model=model)
            suetomoAcc = test(suetomoDir,label=5,imgSize=imgSize,model=model)

        A["ando"].append(andoAcc)
        A["higashi"].append(higashiAcc)
        A["kataoka"].append(kataokaAcc)
        A["kodama"].append(kodamaAcc)
        A["masuda"].append(masudaAcc)
        A["suetomo"].append(suetomoAcc)


    plt.figure()
    plt.plot(range(1, epoch+1), R['trainLoss'], label='trainLoss')
    plt.xlabel('epoch')
    plt.legend()
    plt.savefig(lossPng)
    plt.figure()
    plt.plot(range(1,epoch+1),A["ando"],label="ando")
    plt.plot(range(1,epoch+1),A["higashi"],label="higashi")
    plt.plot(range(1,epoch+1),A["kataoka"],label="kataoka")
    plt.plot(range(1,epoch+1),A["kodama"],label="kodama")
    plt.plot(range(1,epoch+1),A["masuda"],label="masuda")
    plt.plot(range(1,epoch+1),A["suetomo"],label="suetomo")
    plt.xlabel('epoch')
    plt.legend()
    plt.savefig(accPng)
    # Save
    torch.save(model.state_dict(),ptName)