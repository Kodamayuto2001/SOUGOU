from manimlib.imports import *
from sklearn import preprocessing
import cv2 


class NeuralNetworkAnimation(ZoomedScene):
    def construct(self):
        self.__NeuralNetwork(
            inputLayer  = 20,
            hiddenLayer = 16,
            outputLayer = 6,
            neuron      = Dot(),
            # neuron      = Circle(color=WHITE),
            # neuron      = Annulus(inner_radius=0.0,outer_radius=1,color=WHITE).scale(0.1),
            buff        = 0.3,
            isAnimation = 1,
        )
        self.wait(10)

    def __NeuralNetwork(self,inputLayer,hiddenLayer,outputLayer,neuron,buff,isAnimation):
        cnt = 0
        neurons = VGroup()
        forward = VGroup()
        backward= VGroup()
        
        while True:
            if cnt == inputLayer+hiddenLayer+outputLayer+1:
                break

            if cnt <= inputLayer:
                # print(cnt)
                neurons.add(neuron.copy().shift(DOWN*buff*int(cnt-inputLayer/2)).shift(ORIGIN))
            elif cnt <= inputLayer+hiddenLayer:
                # print(cnt)
                neurons.add(neuron.copy().shift(DOWN*buff*int(cnt-(inputLayer+hiddenLayer/2))).shift(RIGHT*2))
            else:
                # print(cnt)
                neurons.add(neuron.copy().shift(DOWN*buff*int(cnt-(inputLayer+hiddenLayer+(outputLayer)/2))).shift(RIGHT*4))
            cnt += 1

        # print(inputLayer+hiddenLayer)

        # forward
        l0 = inputLayer
        while True:
            l1 = hiddenLayer
            while True:
                a = neurons[l0].get_center()
                b = neurons[inputLayer+l1].get_center()
                forward.add(Line(a,b,stroke_width=np.random.randint(0,2,1)))
                if l1 == 1:
                    break
                l1 -= 1
            if l0 == 0:
                break 
            l0 -= 1
        if outputLayer != 0:
            l1 = hiddenLayer
            while True:
                l2 = outputLayer
                while True:
                    a = neurons[inputLayer+l1].get_center()
                    b = neurons[inputLayer+hiddenLayer+l2].get_center()
                    forward.add(Line(a,b,stroke_width=np.random.randint(0,2,1)))
                    if l2 == 1:
                        break
                    l2 -= 1
                if l1 == 1:
                    break
                l1 -= 1
        # print(neurons[0].get_center())
        # print(neurons[20].get_center())

        # backward
        if outputLayer != 0:
            l1 = hiddenLayer
            while True:
                l2 = outputLayer
                while True:
                    a = neurons[inputLayer+l1].get_center()
                    b = neurons[inputLayer+hiddenLayer+l2].get_center()
                    backward.add(Line(b,a,stroke_width=np.random.randint(0,2,1)))
                    if l2 == 1:
                        break
                    l2 -= 1
                if l1 == 1:
                    break
                l1 -= 1
        l0 = inputLayer
        while True:
            l1 = hiddenLayer
            while True:
                a = neurons[l0].get_center()
                b = neurons[inputLayer+l1].get_center()
                backward.add(Line(b,a,stroke_width=np.random.randint(0,2,1)))
                if l1 == 1:
                    break
                l1 -= 1
            if l0 == 0:
                break 
            l0 -= 1

        forward.set_color(color=BLUE)  
        backward.set_color(color=RED)

        andoMaesyori = Preprocessing(
            path    ="assets/Resources/train/ando/0.jpg",
            posX    =5,
            posY    =0,
        )
        andoMaesyori.grayImg()
        andoMaesyori.resizeImg(imgSize=40)
        andoMaesyori.normalizedImg()
        andoMaesyori.vectorImg(imgSize=40,maxText=80,scale=0.2)
##########-----Animation!-----##########
        if isAnimation == 1:
            self.add(neurons)
            # self.add(neurons[0:inputLayer+1+1])
            self.play(Write(forward)) 
            self.play(Write(backward)) 
            # self.targetZoomCam(neurons[inputLayer+1])
            self.play(
                FadeIn(andoMaesyori.imgMob),
            )
            self.play(
                FadeOut(andoMaesyori.imgMob),
                FadeIn(andoMaesyori.imgGrayMob),
            )
            self.play(
                FadeOut(andoMaesyori.imgGrayMob),
                FadeIn(andoMaesyori.imgResizedMob),
            )
            self.play(
                FadeOut(andoMaesyori.imgResizedMob),
                FadeIn(andoMaesyori.imgGroup),
            )
            self.targetZoomCam(target=andoMaesyori.imgGroup[36])
##########-----!Animation-----##########
        pass 

    def targetZoomCam(self,target):
        zoomedCamera        = self.zoomed_camera
        zoomedDisplay       = self.zoomed_display
        frame               = zoomedCamera.frame
        zoomedDisplayFrame  = zoomedDisplay.display_frame

        frame.move_to(target)
        frame.set_color(color=[RED,BLUE])

        zd_rect = BackgroundRectangle(zoomedDisplay, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)
        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomedDisplay))

        self.play(
            Write(frame)
        )
        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation())
        self.play(
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera,
            rate_func=lambda t: smooth(1 - t),
        )
        self.play(
            Uncreate(zoomedDisplayFrame), 
            FadeOut(frame),
        )

        pass 

    

class Preprocessing(Scene):
    def __init__(self,path,posX,posY):
        self.orgImg(path,posX,posY)


    def orgImg(self,path,posX,posY):
        self.img = cv2.imread("assets/Resources/train/ando/0.jpg")
        # RGB
        self.img    = cv2.cvtColor(self.img,cv2.COLOR_BGR2RGB)
        self.imgMob = ImageMobject(self.img)
        self.imgMob.shift(LEFT*posX).shift(UP*posY)
        pass 
    
    def grayImg(self):
        self.imgGray    = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        self.imgGrayMob = ImageMobject(self.imgGray)
        self.imgGrayMob.move_to(self.imgMob)


    def resizeImg(self,imgSize):
        self.imgResized     = cv2.resize(self.imgGray,(imgSize,imgSize))
        self.imgResizedMob  = ImageMobject(self.imgResized)
        self.imgResizedMob.move_to(self.imgGrayMob)

    def normalizedImg(self):
        # print(self.imgResized)
        # [[113 110 113 ...  31  31  35]
        # [116 113 117 ...  31  30  34]
        # [121 116 119 ...  31  29  31]
        # ...
        # [ 36  36  45 ...  93  92  94]
        # [ 33  32  34 ...  95  95  97]
        # [ 32  32  32 ...  94  94  97]]
        mm = preprocessing.MinMaxScaler()
        self.imgNormalized = mm.fit_transform(self.imgResized)
        # print(self.imgNormalized)
        # [[0.47368421 0.42391304 0.39130435 ... 0.01538462 0.05633803 0.12941176]
        # [0.49122807 0.44021739 0.41062802 ... 0.01538462 0.04225352 0.11764706]
        # [0.52046784 0.45652174 0.42028986 ... 0.01538462 0.02816901 0.08235294]
        # ...
        # [0.02339181 0.02173913 0.06280193 ... 0.96923077 0.91549296 0.82352941]
        # [0.00584795 0.         0.00966184 ... 1.         0.95774648 0.85882353]
        # [0.         0.         0.         ... 0.98461538 0.94366197 0.85882353]]

        pass 

    def vectorImg(self,imgSize,maxText,scale):
        try:
            img = np.reshape(self.imgNormalized,(1,imgSize,imgSize))
        except AttributeError:
            img     = np.reshape(self.imgResized,(1,imgSize,imgSize))
        img     = np.transpose(img,(1,2,0))
        img     = self.image_to_vector(img)
        self.imgGroup= Group()
        for i,d in enumerate(img):
            self.imgGroup.add(Text(str(d.tolist()[0]),font="Arial"))
            if i == maxText:
                break
        self.imgGroup.arrange(DOWN,buff=0.2)
        self.imgGroup.move_to(self.imgResizedMob).scale(scale)
        pass 

    def image_to_vector(self,image: np.ndarray) -> np.ndarray:
        """
        Args:
        image: numpy array of shape (length, height, depth)

        Returns:
        v: a vector of shape (length x height x depth, 1)
        """
        length, height, depth = image.shape
        return image.reshape((length * height * depth, 1))
