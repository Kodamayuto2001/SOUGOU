from manimlib.imports import *
import cv2 

class MyAnimation(ZoomedScene):
    def construct(self):
        self.__NeuralNetwork(
            inputLayer  = 20,
            hiddenLayer = 16,
            outputLayer = 6,
            neuron      = Dot(),
            buff        = 0.3
        )
        pass
        self.wait(10)

    def __NeuralNetwork(self,inputLayer,hiddenLayer,outputLayer,neuron,buff):
        cnt = 0
        neurons = VGroup()
        synapse = VGroup()
        
        while True:
            if cnt == inputLayer+hiddenLayer+outputLayer+1:
                break

            if cnt <= inputLayer:
                neurons.add(neuron.copy().shift(DOWN*buff*int(cnt-inputLayer/2)).shift(ORIGIN))
            elif cnt <= inputLayer+hiddenLayer:
                neurons.add(neuron.copy().shift(DOWN*buff*int(cnt-(inputLayer+hiddenLayer/2))).shift(RIGHT*2))
            else:
                neurons.add(neuron.copy().shift(DOWN*buff*int(cnt-(inputLayer+hiddenLayer+(outputLayer)/2))).shift(RIGHT*4))
            cnt += 1

        self.add(neurons)

        l0 = inputLayer
        while True:
            l1 = hiddenLayer
            while True:
                a = neurons[l0].get_center()
                b = neurons[inputLayer+l1].get_center()
                synapse.add(Line(a,b,stroke_width=np.random.randint(0,3,1)))
                if l1 == 1:
                    break
                l1 -= 1
            if l0 == 0:
                break 
            l0 -= 1
        l1 = hiddenLayer
        while True:
            l2 = outputLayer
            while True:
                a = neurons[inputLayer+l1].get_center()
                b = neurons[inputLayer+hiddenLayer+l2].get_center()
                synapse.add(Line(a,b,stroke_width=np.random.randint(1,4,1)))
                if l2 == 1:
                    break
                l2 -= 1
            if l1 == 0:
                break
            l1 -= 1
        self.add(
            synapse
        )               
        pass 

    def __targetZoomCam(self):
        
        pass 



        
