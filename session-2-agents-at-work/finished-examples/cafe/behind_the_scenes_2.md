# Behind the scenes: Demo 2 (the promo video)

**1. The plan.** A storyboard of five 6-second scenes: hello, our number one (Cappuccino),
favourites, busiest day, and the name with opening hours. Every fact came from summary.md
or the brief. No prices, offers or made-up claims.

**2. Tools, in order.**
- *A font check*, to find a rounded typeface on this computer.
- *A Python script with Pillow* (an image library) that draws every frame: coloured backgrounds, circles, a simple cup, and text that fades and slides in. There is no "make video" button, so I drew 900 pictures.
- *ffmpeg*, which joins the pictures into an MP4 that phones and QuickTime can play.
- *ffprobe*, to read the finished file's length and format.

**3. Surprises and changes.**
- Before making the full video, I rendered five test frames. Two needed fixing: a circle crowded the café name, and the favourites scene sat too high. I moved both.
- Rendering took only about 5 seconds, so redoing it was cheap.

**4. How I checked.** ffprobe reports exactly 30.0 seconds, 900 frames, 1080 by 1920,
H.264 in the yuv420p format that QuickTime needs. I decoded the whole file to confirm it has
no errors. Then I pulled one still from the middle of each scene, plus frames from the
cross-fades, and looked at them: all text is large, readable and inside the frame.

I did not open it in QuickTime itself, and stills cannot show how smooth it feels.
