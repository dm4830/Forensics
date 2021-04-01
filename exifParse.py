import exifread
import exif
import sys
import piexif
from exif import Image
lat_mult = 1
long_mult = 1

try:
    with open(sys.argv[1], 'rb') as img:
        exiftags = Image(img)
        exifreadtags = exifread.process_file(img)
        #print(outputtags)
        print("Source File:", sys.argv[1])
        print("Make:", exifreadtags["Image Make"])
        print("Model:", exifreadtags["Image Model"])
        print("Original Date/Time:", exifreadtags["EXIF DateTimeOriginal"])
        lat_direction = str(exifreadtags["GPS GPSLatitudeRef"])
        long_direction = str(exifreadtags["GPS GPSLongitudeRef"])
       
        if lat_direction == "S":
            lat_mult = - 1
        if long_direction == "W":
            long_mult = - 1
        
        lat_degs = int(exiftags.gps_latitude [0])
        lat_min = (exiftags.gps_latitude [1])
        lat_sec = exiftags.gps_latitude[2]

        long_degs = int(exiftags.gps_longitude [0])
        long_min = (exiftags.gps_longitude [1])
        long_sec = exiftags.gps_longitude [2]

        
        print("Latitude:", lat_degs*lat_mult, "degrees,", lat_min, "minutes,", lat_sec, "seconds")
        print("Longitude:", long_degs*long_mult, "degrees,", long_min, "minutes,", long_sec, "seconds")



except FileNotFoundError:
    print("Error! - File Not Found!")
     

except IndexError:
    print("Error! - No Image File Specified!")


