var skia = require('../lib/skia');

paint = new skia.SkPaint();
bitmap = new skia.SkBitmap();
canvas = new skia.SkCanvas();

bitmap.setConfig(1, 800, 600);
bitmap.allocPixels();

//paint.setAntiAlias(true);
//paint.setTextSize(30);

//canvas.setDevice(bitmap);
//canvas.drawColor(1);  //white

//canvas.drawText("Hello World!", 0, 0, paint);

