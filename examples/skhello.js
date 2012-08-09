var skia = require('../lib/skia');

paint = new skia.SkPaint();
bitmap = new skia.SkBitmap();
canvas = new skia.SkCanvas();

bitmap.setConfig(1, 800, 600);
bitmap.allocPixels();

paint.setAntiAlias(true);
paint.setTextSize(30);

//canvas.setBitmapDevice(bitmap);
canvas.drawColor(1);  //white

var string = "Hello World!"
canvas.drawText(string, string.length, 300, 300, paint);

