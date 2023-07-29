def stitch():
        import cv2
        image_paths=['0.jpg','1.jpg','2.jpg','3.jpg','4.jpg']
        # initialized a list of images
        imgs = []

        for i in range(len(image_paths)):
                imgs.append(cv2.imread(image_paths[i]))
                imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)
                # this is optional if your input images isn't too large
                # you don't need to scale down the image
                # in my case the input images are of dimensions 3000x1200
                # and due to this the resultant image won't fit the screen
                # scaling down the images
        # showing the original pictures
        cv2.imshow('1',imgs[0])
        cv2.imshow('2',imgs[1])
        cv2.imshow('3',imgs[2])
        cv2.imshow('4',imgs[3])
        cv2.imshow('5',imgs[4])
        
        stitchy=cv2.Stitcher.create()
        (dummy,output)=stitchy.stitch(imgs)
        
        if dummy != cv2.STITCHER_OK:
        # checking if the stitching procedure is successful
        # .stitch() function returns a true value if stitching is
        # done successfully
                print("stitching ain't successful")
        else:
                print('Your Panorama is ready!!!')
        
        # final output
        cv2.imshow('final result',output)
        
        cv2.waitKey(0)

stitch()
