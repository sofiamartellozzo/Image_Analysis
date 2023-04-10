from Var__noise1 import *

i1 = im1__4__; 
#print(call__make_predictions(i1))
in1, _ = call__make_predictions__adding__noise(i1, 30.0)
cv2.imwrite('/Users/sofia/Desktop/IA&P/Image_Analysis/Ex_21/im1__4__noisy.pgm', in1.reshape((28, 28)))
if1, _ = call__make_predictions__with__filtering(in1)
cv2.imwrite('/Users/sofia/Desktop/IA&P/Image_Analysis/Ex_21/im1__4__filtered.pgm', if1.reshape((28, 28)))