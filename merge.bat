for %%f in (output/*.mp2t) do (
    echo file %%f >> list.txt
)
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4
del list.txt
