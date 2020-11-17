import torchvision.transforms as transforms
import torchvision
import torch
class MyDataLoader:
    r"""
    trainRootDir = "path/to/train/"
    testRootDir = "path/to/test/"
    imgSize = 128
    batchSize = 128
    numWorkers = 3
        --numWorkers = the number of tagNames
    """

    def __init__(self, trainRootDir, testRootDir, imgSize, batchSize,num_workers):
        # self.__my_collate_fn(batch=batchSize)
        self.__dataSet(trainRootDir=trainRootDir, testRootDir=testRootDir,
                       imgSize=imgSize)
        self.__dataLoader(batchSize=batchSize,num_workers=num_workers)
        pass

    def __my_collate_fn(self, batch):
        pass

    def __dataSet(self, trainRootDir, testRootDir, imgSize):
        self.trainData = torchvision.datasets.ImageFolder(root=trainRootDir,
                                                          transform=transforms.Compose([transforms.Grayscale(),transforms.Resize((imgSize,imgSize)),transforms.ToTensor(),#transforms.Normalize((0.5,),(0.5,)),
                                                          ]))
        self.testData = torchvision.datasets.ImageFolder(root=testRootDir,
                                                         transform=transforms.Compose([transforms.Grayscale(),transforms.Resize((imgSize,imgSize)),transforms.ToTensor(),#transforms.Normalize((0.5,),(0.5,)),
                                                         ]))
        pass

    def __dataLoader(self, batchSize,num_workers):
        self.trainDataLoaders = torch.utils.data.DataLoader(self.trainData,
                                                            batch_size=1,
                                                            shuffle=True,num_workers=num_workers)
        self.testDataLoaders = torch.utils.data.DataLoader(self.testData,
                                                           batch_size=1,
                                                           shuffle=True,num_workers=num_workers)
        pass

    def imshow(self):
        print(type(self.trainDataLoaders))
        dataiter = iter(self.trainDataLoaders)
        img, labels = dataiter.next()
        img = torchvision.utils.make_grid(img)
        img = img / 2 + 0.5
        npimg = img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))
        plt.show()
        pass

    def getDataLoaders(self):
        r"""
        RETURN
            --trainDataLoaders,
            --testDataLoaders
        """
        return {"train": self.trainDataLoaders, "test": self.testDataLoaders}

    pass
