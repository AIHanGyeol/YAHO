import time

def jj(start_time , count_time):
    
    if count_time == 0:
        start_time = int(time.time())
    try:
        if start_time + count_time == int(time.time()):
            # cv2.imwrite(f'{image_save_path}/{user_id}_{str(count).zfill(4)}.jpg', image)
            count_time += 10      
    except:
        print('error')  



