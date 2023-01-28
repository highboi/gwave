#convert all png images into gif images for animation frames
for i in *.png; do ffmpeg -y -i "$i" "${i%.*}.gif"; done

#convert all of the gif animation frames into a single animated gif
gifsicle *.gif > output
