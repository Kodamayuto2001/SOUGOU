from manimlib.imports import *
import cv2

class MyAnimation(
    # MovingCameraScene,
    ZoomedScene
    ):
    def construct(self):
        # self.title()
        # self.network(d=Dot())
        # self.network2()
        # self.randomWeightBias()
        # self.loadTrainImgGroup() 
        # self.environmentFadeOut()
        # self.trainData()
        # self.loadTestImgGroup()
        # self.moveCamera1()





        self.network(d=Dot())
        self.randomWeightBias()
        self.trainAnimation()
        self.networkActivation()
        # self.test1()
        # self.test2()
        # self.test3()
        # self.test4()
        # self.test5()

        
    def title(self):
        text = Text("Simple Neural Network",font="Arial",stroke_width=1,size=1.2)

        text.set_color_by_gradient(PINK,GREEN)

        text2= Text("This is Neuron.",font="Arial",stroke_width=1,size=1.2)

        text2.shift(2*UP)

        text2.set_color_by_gradient(RED,YELLOW)

        circle = Circle(color=DARK_BLUE)

        ring = Annulus(inner_radius=0.0,outer_radius=1,color=WHITE)

        n = Dot()

        self.play(Write(text))

        self.wait(1)

        self.play(FadeOut(text))

        self.remove(text)

        self.wait()

        self.play(ShowCreation(circle))

        self.play(FadeOut(circle),FadeIn(ring))

        self.wait(1)

        self.play(Write(text2))

        self.wait(1)

        self.play(FadeOut(ring),FadeIn(n))

        self.play(FadeOut(text2))

    def network(self,d):
        self.n0 = []
        self.n1 = []
        self.n2 = []
        cnt = 0
        while True:
            self.n0.append(d.copy())
            if cnt == 20:
                break 
            cnt += 1
        cnt = 0
        while True:
            self.n1.append(d.copy())
            if cnt == 16:
                break
            cnt += 1
        cnt = 0
        while True:
            self.n2.append(d.copy())
            if cnt == 5:
                break
            cnt += 1



        self.play(
            #####-----input-----#####
            self.n0[10].shift,UP*0.3*10,ORIGIN,
            self.n0[9].shift,UP*0.3*9,ORIGIN,
            self.n0[8].shift,UP*0.3*8,ORIGIN,
            self.n0[7].shift,UP*0.3*7,ORIGIN,
            self.n0[6].shift,UP*0.3*6,ORIGIN,
            self.n0[5].shift,UP*0.3*5,ORIGIN,
            self.n0[4].shift,UP*0.3*4,ORIGIN,
            self.n0[3].shift,UP*0.3*3,ORIGIN,
            self.n0[2].shift,UP*0.3*2,ORIGIN,
            self.n0[1].shift,UP*0.3*1,ORIGIN,
            self.n0[0].shift,UP*0.3*0,ORIGIN,

            self.n0[20].shift,DOWN*0.3*10,ORIGIN,
            self.n0[19].shift,DOWN*0.3*9,ORIGIN,
            self.n0[18].shift,DOWN*0.3*8,ORIGIN,
            self.n0[17].shift,DOWN*0.3*7,ORIGIN,
            self.n0[16].shift,DOWN*0.3*6,ORIGIN,
            self.n0[15].shift,DOWN*0.3*5,ORIGIN,
            self.n0[14].shift,DOWN*0.3*4,ORIGIN,
            self.n0[13].shift,DOWN*0.3*3,ORIGIN,
            self.n0[12].shift,DOWN*0.3*2,ORIGIN,
            self.n0[11].shift,DOWN*0.3*1,ORIGIN,


            #####-----hiden-----#####
            self.n1[8].shift,UP*0.3*8,RIGHT*2,
            self.n1[7].shift,UP*0.3*7,RIGHT*2,
            self.n1[6].shift,UP*0.3*6,RIGHT*2,
            self.n1[5].shift,UP*0.3*5,RIGHT*2,
            self.n1[4].shift,UP*0.3*4,RIGHT*2,
            self.n1[3].shift,UP*0.3*3,RIGHT*2,
            self.n1[2].shift,UP*0.3*2,RIGHT*2,
            self.n1[1].shift,UP*0.3*1,RIGHT*2,
            self.n1[0].shift,UP*0.3*0,RIGHT*2,

            self.n1[16].shift,DOWN*0.3*8,RIGHT*2,
            self.n1[15].shift,DOWN*0.3*7,RIGHT*2,
            self.n1[14].shift,DOWN*0.3*6,RIGHT*2,
            self.n1[13].shift,DOWN*0.3*5,RIGHT*2,
            self.n1[12].shift,DOWN*0.3*4,RIGHT*2,
            self.n1[11].shift,DOWN*0.3*3,RIGHT*2,
            self.n1[10].shift,DOWN*0.3*2,RIGHT*2,
            self.n1[9].shift,DOWN*0.3*1,RIGHT*2,


            #####-----output-----#####
            self.n2[2].shift,UP*0.3*2,RIGHT*4,
            self.n2[1].shift,UP*0.3*1,RIGHT*4,
            self.n2[0].shift,UP*0.3*0,RIGHT*4,
            self.n2[5].shift,DOWN*0.3*3,RIGHT*4,
            self.n2[4].shift,DOWN*0.3*2,RIGHT*4,
            self.n2[3].shift,DOWN*0.3*1,RIGHT*4,
        )
        self.wait()
        
    def network2(self):
        text = Text("Input Layer")
        text.move_to(LEFT).to_edge(UP*0.8)
        self.play(Write(text))
        self.wait()
        text2 = Text("Hidden Layer")
        text2.move_to(RIGHT*2.75).to_edge(DOWN)
        self.play(Write(text2))
        self.wait()
        text3 = Text("Output Layer")
        text3.move_to(RIGHT*5).to_edge(UP*5)
        self.play(Write(text3))
        self.wait()

        self.play(FadeOut(text))
        # self.wait()
        self.play(FadeOut(text2))
        # self.wait()
        self.play(FadeOut(text3))
        self.wait(1)

    def randomWeightBias(self):
        text = TexMobject("Random\\\\","weight") 
        text.move_to(LEFT*3).to_edge(UP*2)

        self.line = VGroup()
        
        l0 = 20
        while True:
            l1 = 16
            while True:
                a = self.n0[l0].get_center()
                b = self.n1[l1].get_center()
                self.line.add(Line(a,b,stroke_width=np.random.randint(0,3,1)))
                if l1 == 0:
                    break
                l1 -= 1
            if l0 == 0:
                break 
            l0 -= 1

        l1 = 16
        while True:
            l2 = 5
            while True:
                a = self.n1[l1].get_center()
                b = self.n2[l2].get_center()
                self.line.add(Line(a,b,stroke_width=np.random.randint(1,4,1)))
                if l2 == 0:
                    break
                l2 -= 1
            if l1 == 0:
                break 
            l1 -= 1

        self.play(
            # Write(text),
            Write(self.line)
        )
        self.wait(2)  


        mColor = [LIGHT_BROWN,BLUE,TEAL,GREEN,YELLOW,GOLD,RED,MAROON,PURPLE,WHITE,PINK,ORANGE]

        # print(np.random.randint(0,12,1))
        # print(type(np.random.randint(0,12,1)))
        # print(int(np.random.randint(0,12,1)))
        # print(len(self.n0))
        # print(len(self.n1))
        # print(len(self.n2))
        
        cnt_n0 = int(len(self.n0))
        cnt_n1 = int(len(self.n1))
        cnt_n2 = int(len(self.n2))

        # self.play(
        #     text[1].become,TexMobject(
        #         "bias",
        #         tex_to_color_map={
        #         "b": BLUE_C,
        #         "i": GOLD_C,
        #         "a": PINK,
        #         "s": PURPLE,
        #     },
        #     ).move_to(text[1]),
        #     run_time=2,
        # )
        while True:
            cnt_n0 -= 1
            self.n0[cnt_n0].set_color(color=mColor[int(np.random.randint(0,12,1))])
            if cnt_n0 == 0:
                break
        while True:
            cnt_n1 -= 1
            self.n1[cnt_n1].set_color(color=mColor[int(np.random.randint(0,12,1))])
            if cnt_n1 == 0:
                break

        while True:
            cnt_n2 -= 1
            self.n2[cnt_n2].set_color(color=mColor[int(np.random.randint(0,12,1))])
            if cnt_n2 == 0:
                break
        
        # self.wait(2)
        # self.play(FadeOut(text))
        
        # self.wait()


        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        self.all_words = VGroup(
            TextMobject(
                # "You have a\\\\", 
                "Development environment \\\\",
            ),
            TextMobject(
                "Python\\\\",
            ).set_color_by_gradient(YELLOW,BLUE_C),
            TexMobject(
                "Anaconda\\\\",
            ).set_color(GREEN),
            TexMobject(
                "PyTorch\\\\"
            ).set_color_by_gradient(RED,WHITE),
            TexMobject(
                "Animation : manim",
            ).set_color_by_gradient(logo_green, logo_blue, logo_red),
        )

    
        # self.all_words.arrange(DOWN)
        # self.all_words.move_to(LEFT*3.5).to_edge(UP*3)
        # # self.add(self.all_words)
        # self.play(Write(self.all_words))
        # self.loadManimLogo()        
        # self.play(FadeOut(self.all_words))
        pass 

    def loadManimLogo(self):
        self.manimLogo = ImageMobject("logo/cropped.png")
        self.manimLogo.scale(1.0)
        self.manimLogo.shift(LEFT*3.5).shift(DOWN*2.25)
        self.play(FadeIn(self.manimLogo))
        # self.play(FadeOut(self.manimLogo))

    def environmentFadeOut(self):
        self.play(FadeOut(self.manimLogo))
        self.play(FadeOut(self.all_words))

    # def loadImg(self):
    #     # group = Group(image,text).arrange(DOWN)
    #     # self.img = ImageMobject("assets/images/lena.jpeg")
    #     self.img = ImageMobject("assets/Resources/train/kodama/39.jpg")
    #     self.img.scale(1.5)
    #     self.img.shift(LEFT*10)

    #     self.play(ShowCreation(self.img))

    #     # self.img = Group(
    #     #     ImageMobject("assets/Resources/train/kodama/39.jpg").scale(1.5).shift(LEFT*10),
    #     #     Text("3",font="Arial",stroke_width=1,size=1.2).shift(LEFT*5),
    #     # )

    #     # self.play(ShowCreation(self.img))
    #     pass 

    # def loadImg2(self):
    #     self.img2 = ImageMobject("assets/Resources/train/kodama/0.jpg")
    #     self.img2.scale(1.5)
    #     self.img2.move_to(self.img)

    #     self.play(FadeIn(self.img2))

    def loadTrainImgGroup(self):
        self.andoTrainImg    = Group()
        self.higashiTrainImg = Group()
        self.kataokaTrainImg = Group()
        self.kodamaTrainImg  = Group()
        self.masudaTrainImg  = Group()
        self.suetomoTrainImg = Group()


        self.andoTrainImg.add(
            ImageMobject("assets/Resources/train/ando/0.jpg").scale(1.5).shift(LEFT*10).shift(UP*15),
            # ImageMobject("assets/Resources/train/ando/15.jpg").scale(1.5).shift(LEFT*10).shift(UP*15),
            # ImageMobject("assets/Resources/train/ando/31.jpg").scale(1.5).shift(LEFT*10).shift(UP*15),
            # ImageMobject("assets/Resources/train/ando/47.jpg").scale(1.5).shift(LEFT*10).shift(UP*15),
            # ImageMobject("assets/Resources/train/ando/63.jpg").scale(1.5).shift(LEFT*10).shift(UP*15),
        )
        self.play(ShowCreation(self.andoTrainImg[0]))

        self.higashiTrainImg.add(
            ImageMobject("assets/Resources/train/higashi/0.jpg").scale(1.5).shift(LEFT*10).shift(UP*10),
            # ImageMobject("assets/Resources/train/higashi/15.jpg").scale(1.5).shift(LEFT*10).shift(UP*10),
            # ImageMobject("assets/Resources/train/higashi/31.jpg").scale(1.5).shift(LEFT*10).shift(UP*10),
            # ImageMobject("assets/Resources/train/higashi/47.jpg").scale(1.5).shift(LEFT*10).shift(UP*10),
            # ImageMobject("assets/Resources/train/higashi/63.jpg").scale(1.5).shift(LEFT*10).shift(UP*10),
        )
        self.play(ShowCreation(self.higashiTrainImg[0]))

        self.kataokaTrainImg.add(
            ImageMobject("assets/Resources/train/kataoka/0.jpg").scale(1.5).shift(LEFT*10).shift(UP*5),
            # ImageMobject("assets/Resources/train/kataoka/15.jpg").scale(1.5).shift(LEFT*10).shift(UP*5),
            # ImageMobject("assets/Resources/train/kataoka/31.jpg").scale(1.5).shift(LEFT*10).shift(UP*5),
            # ImageMobject("assets/Resources/train/kataoka/47.jpg").scale(1.5).shift(LEFT*10).shift(UP*5),
            # ImageMobject("assets/Resources/train/kataoka/63.jpg").scale(1.5).shift(LEFT*10).shift(UP*5),
        )
        self.play(ShowCreation(self.kataokaTrainImg[0]))

        self.kodamaTrainImg.add(
            ImageMobject("assets/Resources/train/kodama/0.jpg").scale(1.5).shift(LEFT*10),
            ImageMobject("assets/Resources/train/kodama/15.jpg").scale(1.5).shift(LEFT*10),
            ImageMobject("assets/Resources/train/kodama/31.jpg").scale(1.5).shift(LEFT*10),
            ImageMobject("assets/Resources/train/kodama/47.jpg").scale(1.5).shift(LEFT*10),
            ImageMobject("assets/Resources/train/kodama/63.jpg").scale(1.5).shift(LEFT*10),
        )
        self.play(FadeIn(self.kodamaTrainImg[0]))

        self.masudaTrainImg.add(
            ImageMobject("assets/Resources/train/masuda/0.jpg").scale(1.5).shift(LEFT*10).shift(DOWN*5),
            # ImageMobject("assets/Resources/train/masuda/15.jpg").scale(1.5).shift(LEFT*10).shift(DOWN*5),
            # ImageMobject("assets/Resources/train/masuda/31.jpg").scale(1.5).shift(LEFT*10).shift(DOWN*5),
            # ImageMobject("assets/Resources/train/masuda/47.jpg").scale(1.5).shift(LEFT*10).shift(DOWN*5),
            # ImageMobject("assets/Resources/train/masuda/63.jpg").scale(1.5).shift(LEFT*10).shift(DOWN*5),
        )
        self.play(ShowCreation(self.masudaTrainImg[0]))

        self.suetomoTrainImg.add(
            ImageMobject("assets/Resources/train/suetomo/0.jpg").scale(1.5).shift(LEFT*10).shift(DOWN*10),
            # ImageMobject("assets/Resources/train/suetomo/15.jpg").scale(1.5).shift(LEFT*10).shift(DOWN*10),
            # ImageMobject("assets/Resources/train/suetomo/31.jpg").scale(1.5).shift(LEFT*10).shift(DOWN*10),
            # ImageMobject("assets/Resources/train/suetomo/47.jpg").scale(1.5).shift(LEFT*10).shift(DOWN*10),
            # ImageMobject("assets/Resources/train/suetomo/63.jpg").scale(1.5).shift(LEFT*10).shift(DOWN*10),
        )
        self.play(ShowCreation(self.suetomoTrainImg[0]))


    def trainData(self):
        self.play(
            self.camera_frame.move_to,self.kodamaTrainImg,
            self.camera_frame.set_width,self.kodamaTrainImg.get_width()*2
        )
        self.wait(2.0)
        self.play(
            self.camera_frame.set_width,self.kodamaTrainImg.get_width()*4,
        )
        
        text = TextMobject(
            "data\\\\",
            "(",
            "$\\text{ANYpx} \\times \\text{ANYpx}$",
            ")",
            font="Arial",
            stroke_width=1,
            size=1.2
        )
        text.set_color_by_gradient(PURPLE,ORANGE)
        text.move_to(self.kodamaTrainImg)
        text.shift(UP*2.5)

        self.play(Write(text))
        self.wait(1)
        # self.play(FadeOut(text))

        self.play(
            self.camera_frame.shift,RIGHT*2.5,
        )

        text2 = TexMobject("label",font="Arial",stroke_width=1,size=1.2)
        text2.set_color_by_gradient(BLUE_C,DARK_BLUE)
        text2.move_to(text)
        text2.shift(RIGHT*5)

        self.play(Write(text2))

        text3 = TexMobject("3",font="Arial",stroke_width=1,size=1.2)
        text3.set_color(BLUE_C)
        text3.move_to(self.kodamaTrainImg)
        text3.shift(RIGHT*5)

        self.play(Write(text3))

        # print(len(self.kodamaTrainImg)) -> 2
        cnt = 0
        while True:
            tmp = self.kodamaTrainImg[cnt+1]
            tmp.move_to(self.kodamaTrainImg[cnt])
            self.play(FadeIn(tmp))
            # self.wait()
            cnt += 1
            if cnt+1 == int(len(self.kodamaTrainImg)):
                break

        self.play(
            text[0].become,TextMobject(
                "80 sheets",
            ).move_to(text[0]),
            run_time=2,
        )

        self.play(FadeOut(text),FadeOut(text2))

        self.play(
            text3[0].become,TextMobject(
                "3",
            ).scale(5).move_to(text3[0]),
            text3[0].copy().shift(UP*5).become,TextMobject(
                "2",
            ).scale(5).move_to(text3[0].copy().shift(UP*5)),
            text3[0].copy().shift(UP*10).become,TextMobject(
                "1",
            ).scale(5).move_to(text3[0].copy().shift(UP*10)),
            text3[0].copy().shift(UP*15).become,TextMobject(
                "0",
            ).scale(5).move_to(text3[0].copy().shift(UP*15)),
            text3[0].copy().shift(DOWN*5).become,TextMobject(
                "4",
            ).scale(5).move_to(text3[0].copy().shift(DOWN*5)),
            text3[0].copy().shift(DOWN*10).become,TextMobject(
                "5",
            ).scale(5).move_to(text3[0].copy().shift(DOWN*10)),
            self.camera_frame.set_width,self.kodamaTrainImg.get_width()*20,
            self.camera_frame.shift,UP*2.5,
        )

        # text4 = TextMobject(
        #     "$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$,
        # ).shift(UP*15).scale(5)
        text4=TextMobject("$\\text{80} \\times \\text{6} $")
        text4.shift(UP*15).scale(5).shift(LEFT*30)

        print(self.kodamaTrainImg.get_left())
        print(self.kodamaTrainImg.get_width()/2)

        self.play(
            Write(text4),
        )
        self.play(
            text4[0].become,TextMobject(
                "$\\text{480}$",
                " sheets"
            ).move_to(text4[0]).scale(5),
            run_time=2,
        )

        self.textTrain = TextMobject("Train\\\\data").shift(DOWN*5).scale(10).shift(LEFT*25)

        self.play(Write(self.textTrain))

        self.wait(2)

        # self.play(
        #     self.camera_frame.move_to, ORIGIN,
        #     self.camera_frame.set_width,14,
        # )
        pass 


    def loadTestImgGroup(self):
        # width -> -10

        # height
        # print(self.andoTrainImg.get_center()[1])     -> 15.0
        # print(self.higashiTrainImg.get_center()[1])  -> 10.0  
        # print(self.kataokaTrainImg.get_center()[1])  -> 5.0
        # print(self.kodamaTrainImg.get_center()[1])   -> 0.0
        # print(self.masudaTrainImg.get_center()[1])   -> -5.0
        # print(self.suetomoTrainImg.get_center()[1])  -> -10.0

        self.andoTestImg    = Group()
        self.higashiTestImg = Group()
        self.kataokaTestImg = Group()
        self.kodamaTestImg  = Group()
        self.masudaTestImg  = Group()
        self.suetomoTestImg = Group()

        testShiftDown = 15.0

        self.andoTestImg.add(
            ImageMobject("assets/Resources/test/ando/80.jpg").scale(1.5).shift(float(self.andoTrainImg.get_center()[0])).shift(DOWN*(float(self.andoTrainImg.get_center()[1]+testShiftDown)))
        )
        # self.play(FadeIn(self.andoTestImg[0]))

        self.higashiTestImg.add(
            ImageMobject("assets/Resources/test/higashi/80.jpg").scale(1.5).shift(float(self.higashiTrainImg.get_center()[0])).shift(DOWN*(float(self.higashiTrainImg.get_center()[1]+testShiftDown)))
        )
        # self.play(FadeIn(self.higashiTestImg[0]))

        self.kataokaTestImg.add(
            ImageMobject("assets/Resources/test/kataoka/80.jpg").scale(1.5).shift(float(self.kataokaTrainImg.get_center()[0])).shift(DOWN*(float(self.kataokaTrainImg.get_center()[1]+testShiftDown)))
        )
        # self.play(FadeIn(self.kataokaTestImg[0]))

        self.kodamaTestImg.add(
            ImageMobject("assets/Resources/test/kodama/80.jpg").scale(1.5).shift(float(self.kodamaTrainImg.get_center()[0])).shift(DOWN*float(self.kodamaTrainImg.get_center()[1]+testShiftDown))
        )
        # self.play(FadeIn(self.kodamaTestImg[0]))

        self.masudaTestImg.add(
            ImageMobject("assets/Resources/test/masuda/80.jpg").scale(1.5).shift(float(self.masudaTrainImg.get_center()[0])).shift(DOWN*float(self.masudaTrainImg.get_center()[1]+testShiftDown))
        )
        # self.play(FadeIn(self.masudaTestImg[0]))

        self.suetomoTestImg.add(
            ImageMobject("assets/Resources/test/suetomo/80.jpg").scale(1.5).shift(float(self.suetomoTrainImg.get_center()[0])).shift(DOWN*float(self.suetomoTrainImg.get_center()[1]+testShiftDown))
        )
        # self.play(FadeIn(self.suetomoTestImg[0]))

        # print(self.textTrain.get_center()) -> [-25.  -5.   0.]
        self.textTest = TextMobject("Test\\\\data").shift(DOWN*(5+int(testShiftDown))).scale(10).shift(LEFT*25)

        textSheets = TextMobject("120 sheets")
        textSheets.shift(DOWN*15*2).scale(5).shift(LEFT*30)

        testlabel = TexMobject("0",font="Arial",stroke_width=1,size=1.2)
        testlabel.set_color(WHITE)
        testlabel.move_to(self.andoTestImg)
        testlabel.shift(RIGHT*5)


        self.play(
            ShowCreation(self.andoTestImg[0]),
            ShowCreation(self.higashiTestImg[0]),
            ShowCreation(self.kataokaTestImg[0]),
            ShowCreation(self.kodamaTestImg[0]),
            ShowCreation(self.masudaTestImg[0]),
            ShowCreation(self.suetomoTestImg[0]),

            Write(self.textTest),

            Write(textSheets),
        )
        self.play(
            Write(testlabel.scale(5)),
            testlabel[0].copy().shift(UP*5).become,TextMobject(
                "1",
            ).scale(5).move_to(testlabel[0].copy().shift(UP*5)),
            testlabel[0].copy().shift(UP*10).become,TextMobject(
                "2",
            ).scale(5).move_to(testlabel[0].copy().shift(UP*10)),
            testlabel[0].copy().shift(UP*15).become,TextMobject(
                "3",
            ).scale(5).move_to(testlabel[0].copy().shift(UP*15)),
            testlabel[0].copy().shift(UP*20).become,TextMobject(
                "4",
            ).scale(5).move_to(testlabel[0].copy().shift(UP*20)),
            testlabel[0].copy().shift(UP*25).become,TextMobject(
                "5",
            ).scale(5).move_to(testlabel[0].copy().shift(UP*25)),

            self.camera_frame.set_width,self.kodamaTestImg.get_width()*20,
            self.camera_frame.move_to,self.kodamaTestImg.get_center(),
        )        
        
        
        self.wait(2)
        pass 

    def moveCamera1(self):
        self.play(
            self.camera_frame.move_to,
            self.andoTrainImg,
            self.camera_frame.set_width,
            self.andoTrainImg.get_width()*2,
        )
        self.wait()
        pass 

    def trainAnimation(self):
        img = cv2.imread("assets/Resources/train/ando/0.jpg")
        # RGB
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        imgMob = ImageMobject(img)
        imgMob.shift(LEFT*5)

        imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        imgGrayMob = ImageMobject(imgGray)
        imgGrayMob.shift(LEFT*5)

        # リサイズ
        img = cv2.resize(imgGray,(40,40))
        imgResizedMob = ImageMobject(img)
        imgResizedMob.shift(LEFT*5)

        b1 = Brace(imgResizedMob, direction=RIGHT)
        b1text = b1.get_text("40 px")
        b2 = Brace(imgResizedMob,direction=DOWN)
        b2text = b2.get_text("40 px")

        # リシェイプ
        img = np.reshape(img,(1,40,40))
        imgReshapeMob = ImageMobject(img)
        imgReshapeMob.shift(LEFT*5)

        # transpose h,c,w
        img = np.transpose(img,(1,2,0))
        imgTPMob = ImageMobject(img)
        imgTPMob.shift(LEFT*5)

        # toVector
        img = self.image_to_vector(img)

        imgGroup = Group()

        for i,d in enumerate(img):
            imgGroup.add(Text(str(d.tolist()[0])))
            if i == 100:
                break

        imgGroup.arrange(DOWN, buff=0.2)

        text = TexMobject(
            "\\text{Image Loading }",
            font="Arial",
            stroke_width=1,
            size=1.2,
        ).shift(LEFT*5).shift(UP*2.0)
        

        self.play(
            Write(
                text
            ),
            FadeIn(imgMob),
        )

        self.wait(1)

        self.play(
            text[0].become,TexMobject(
                "\\text{Grayscale }",
                font="Arial",
                stroke_width=1,
                size=1.2,
            ).shift(LEFT*5).shift(UP*2.0),
            FadeIn(imgGrayMob),
        )

        self.wait(1)

        self.play(
            text[0].become,TexMobject(
                "\\text{Resize }",
                font="Arial",
                stroke_width=1,
                size=1.2,
            ).shift(LEFT*5).shift(UP*2.0),
            FadeIn(imgResizedMob),
            ShowCreation(b1),
            ShowCreation(b1text),
            ShowCreation(b2),
            ShowCreation(b2text),
        )

        self.wait(1)


        self.play(
            text[0].become,TexMobject(
                "\\text{Reshape }",
                "\\\\",
                "\\text{transpose }",
                font="Arial",
                stroke_width=1,
                size=1.2,
            ).arrange(DOWN, center=False, aligned_edge = LEFT, buff=0.0).shift(LEFT*5).shift(UP*2.0),
            FadeIn(imgTPMob),
        )

        self.wait(1)

        self.play(
            # ToTensor 正規化される
            text[0].become,TexMobject(
                "\\text{ToTensor() }",
                "\\\\",
                "\\text{    == Normalized }",
                font="Arial",
                stroke_width=1,
                size=1.2,
            ).arrange(DOWN, center=False, aligned_edge = LEFT, buff=0.0).shift(LEFT*5).shift(UP*2.0),
        )

        self.wait(1)

        self.play(
            FadeOut(b1),
            FadeOut(b1text),
            FadeOut(b2),
            FadeOut(b2text),

            # view(-1, 40*40)
            text[0].become,TexMobject(
                "\\text{view(-1, 40*40) }",
                "\\\\",
                "\\text{    == vector }",
                font="Arial",
                stroke_width=1,
                size=1.2,
            ).arrange(DOWN, center=False, aligned_edge = LEFT, buff=0.0).shift(LEFT*5).shift(UP*2.0),
        )

        self.remove(
            imgMob,
            imgGrayMob,
            imgResizedMob,
            imgReshapeMob,
        )

        textVector = TexMobject("Vector").shift(LEFT*3).shift(UP*2.0)

        self.play(
            FadeOut(imgTPMob),
            Write(textVector),
            FadeIn(imgGroup.shift(LEFT*5).scale(0.2)),
            text[0].become,imgGroup[0].move_to(LEFT*5).scale(0.2),run_time=2,
        )

        self.test3(imgGroup)

        ano = Arrow(start=[-3, 0, 0], end=[-1, 0, 0], color=WHITE)

        self.play(FadeIn(ano))

        self.wait()

        self.play(FadeOut(imgGroup))

        self.play(FadeOut(textVector))

        # self.wait()

        self.play(FadeOut(ano))

        # self.wait(3)

    def networkActivation(self):
        l0 = 20
        self.line1 = VGroup()
        while True:
            l1 = 16
            while True:
                a = self.n0[l0].get_center()
                b = self.n1[l1].get_center()
                self.line1.add(Line(a,b,stroke_width=np.random.randint(0,3,1)))
                if l1 == 0:
                    break
                l1 -= 1
            if l0 == 0:
                break 
            l0 -= 1

        l1 = 16
        while True:
            l2 = 5
            while True:
                a = self.n1[l1].get_center()
                b = self.n2[l2].get_center()
                self.line1.add(Line(a,b,stroke_width=np.random.randint(1,4,1)))
                if l2 == 0:
                    break
                l2 -= 1
            if l1 == 0:
                break 
            l1 -= 1

        text = TexMobject(
            "\\text{Forward }",
            font="Arial",
            stroke_width=1,
            size=1.2,
        ).shift(RIGHT*5).shift(UP*2.5)
        ano1 = Arrow(start=[4, -2, 0], end=[6, -2, 0], color=WHITE)
        ano2 = Arrow(start=[6, -2, 0], end=[4, -2, 0], color=WHITE)
        
        self.line1.set_color(color=[PINK,YELLOW])
        self.play(
            Write(text),
            FadeIn(ano1),
            Write(self.line1)
        )
        self.wait()

        self.play(
            FadeIn(ano2),FadeOut(ano1),
            text[0].become,TexMobject(
                "\\text{Backward }",
                font="Arial",
                stroke_width=1,
                size=1.2,
            ).shift(RIGHT*5).shift(UP*2.5),
            run_time=2,
        )
        self.play(Write(self.line))

        ando = TexMobject("tensor([[-1.4741,\\\\ -2.1356,\\\\ -1.5679,\\\\ -1.7038,\\\\ -1.7193,\\\\ -2.4870]])",size=0.8).shift(LEFT*5)

        pAndo = TexMobject("\\text{Ando    accuracy : 9.5 }\\%",size=0.6).shift(LEFT*3.5).shift(DOWN*3)


        self.play(Write(ando),FadeOut(ano2),FadeOut(text))
        self.play(Write(pAndo))
        self.play(
            FadeOut(ando),
            # FadeOut(pAndo),
            pAndo[0].become,TexMobject(
                "\\text{Higashi    accuracy : 0.0 }\\%",
                size=0.6,
            ).move_to(pAndo[0]),
        )

        self.play(
            pAndo[0].become,TexMobject(
                "\\text{Kataoka    accuracy : 0.0 }\\%",
                size=0.6,
            ).move_to(pAndo[0]),
        )

        self.play(
            pAndo[0].become,TexMobject(
                "\\text{Kodama    accuracy : 10.0 }\\%",
                size=0.6,
            ).move_to(pAndo[0]),
        )

        self.play(
            pAndo[0].become,TexMobject(
                "\\text{Masuda    accuracy : 1.0 }\\%",
                size=0.6,
            ).move_to(pAndo[0]),
        )


        self.play(
            pAndo[0].become,TexMobject(
                "\\text{Suetomo    accuracy : 9.5 }\\%",
                size=0.6,
            ).move_to(pAndo[0]),
        )

        self.play(
            Write(Text("loop").shift(LEFT*5).shift(UP*2))
        )

        self.wait(2)
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

    def test1(self):
        img = cv2.imread("assets/Resources/train/ando/0.jpg")
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img = cv2.resize(imgGray,(40,40))
        img = np.reshape(img,(1,40,40))
        img = np.transpose(img,(1,2,0))
        img = self.image_to_vector(img)


        imgGroup = Group()
        # imgGroup.add(Text(str(img.tolist()[1][0])))

        for i,d in enumerate(img):
            imgGroup.add(Text(str(d.tolist()[0])))
            if i == 100:
                break
        
        imgGroup.arrange(DOWN, buff=0.2)

        self.play(
            FadeIn(imgGroup.shift(LEFT*1.5).scale(0.2))
        )

        self.wait()

        self.play(
            imgGroup.shift(LEFT*1.5).scale(0.2).become,imgGroup.move_to(ORIGIN),run_time=2
        )

        self.wait()
        pass 

    def test2(self):
        dot = Dot().set_color(GREEN)
        sq = Circle(fill_opacity=1, radius=0.2).next_to(dot, RIGHT)
        self.add(dot, sq)
        self.wait(1)
        self.activate_zooming(animate=False)
        self.wait(1)
        self.play(dot.shift, LEFT * 0.3)

        # self.play(self.zoomed_camera.frame.scale, 4)
        # self.play(self.zoomed_camera.frame.shift, 0.5 * DOWN)
        pass 

    def test3(self,img):
        # dot = Dot().shift(UL * 2)
        # image = ImageMobject("assets/Resources/train/ando/0.jpg")
        # image.set_height(5)
        # frame_text = Text("Frame", color=BLACK).scale(1.4)
        # zoomed_camera_text = Text("Zoomed camera", color=BLACK).scale(1.4)

        # self.add(
        #     img, 
        #     # dot,
        # )
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(img)
        frame.set_color(DARK_BLUE)
        zoomed_display_frame.set_color(WHITE)
        zoomed_display.shift(DOWN)

        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)

        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))

        # frame_text.next_to(frame, DOWN)

        self.play(
            ShowCreation(frame), 
            # FadeInFrom(frame_text, direction=DOWN),
        )
        self.activate_zooming()

        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
        # zoomed_camera_text.next_to(zoomed_display_frame, DOWN)
        # self.play(FadeInFrom(zoomed_camera_text, direction=DOWN))
        # Scale in        x   y  z
        scale_factor = [0.5, 0.5, 0]
        self.play(
            frame.scale, scale_factor,
            zoomed_display.scale, scale_factor,
            # FadeOut(zoomed_camera_text),
            # FadeOut(frame_text)
        )
        self.wait()
        # self.play(ScaleInPlace(zoomed_display, 2))
        # self.wait()
        self.play(frame.shift, 2.5 * DOWN)
        self.wait()
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        self.remove(img)
        self.wait()

    def test4(self):
        ano1 = Arrow(start=[4, -2, 0], end=[6, -2, 0], color=WHITE)
        self.play(FadeIn(ano1))
        self.wait(1)

        ano2 = Arrow(start=[6, -2, 0], end=[4, -2, 0], color=WHITE)
        self.play(FadeIn(ano2),FadeOut(ano1))
        self.wait(2)
        pass 


    def test5(self):
        ando = TexMobject("tensor([[-1.4741,\\\\ -2.1356,\\\\ -1.5679,\\\\ -1.7038,\\\\ -1.7193,\\\\ -2.4870]])",size=0.8).shift(LEFT*5)

        pAndo = TexMobject("\\text{Ando    accuracy : 9.5 }\\%",size=0.6).shift(LEFT*3.5).shift(DOWN*3)

        self.play(Write(ando))
        self.play(Write(pAndo))

        self.wait()


