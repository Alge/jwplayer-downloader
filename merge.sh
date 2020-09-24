for f in output/*.mp2t ; do echo file \'$f\' >> list.txt; done && ffmpeg -f concat -safe 0 -i list.txt -c copy stitched-video.mp4 && rm list.txt
