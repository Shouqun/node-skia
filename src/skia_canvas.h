#ifndef NODE_SKIA_CANVAS_H_
#define NODE_SKIA_CANVAS_H_

#include <v8.h>
#include <node.h>
#include <node_object_wrap.h>
#include <node_version.h>

#include "SkCanvas.h"
#include "SkPaint.h"

class NodeSkiaCanvas : public node::ObjectWrap {
public:
  static void Initialize(v8::Handle<v8::Object> target);
  static v8::Handle<v8::Value> New(const v8::Arguments &args);
  static v8::Handle<v8::Value> DrawColor(const v8::Arguments &args);
  static v8::Handle<v8::Value> DrawText(const v8::Arguments &args);
  static v8::Handle<v8::Value> SetBitmapDevice(const v8::Arguments &args);

  static v8::Persistent<v8::Function> constructor;

public:
  NodeSkiaCanvas();
  ~NodeSkiaCanvas();

  void DrawColor(SkColor color) { canvas_->drawColor(color); };
  void DrawText(const void* text, size_t byteLength,
                SkScalar x, SkScalar y, const SkPaint& paint);
  void SetBitmapDevice(const SkBitmap& bitmap) {
    canvas_->setBitmapDevice(bitmap);
  }

private:
  SkCanvas *canvas_;
};

#endif
