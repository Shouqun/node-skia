#include "skia_canvas.h"

#include <v8.h>
#include <node.h>
#include <node_object_wrap.h>

#include "SkCanvas.h"
#include "SkPaint.h"

#include "skia_bitmap.h"
#include "skia_paint.h"

using namespace v8;
using namespace node;

Persistent<Function> NodeSkiaCanvas::constructor;

NodeSkiaCanvas::NodeSkiaCanvas() {
  canvas_ = new SkCanvas();
}

NodeSkiaCanvas::~NodeSkiaCanvas() {
}

void NodeSkiaCanvas::Initialize(Handle<Object> target) {
  Local<FunctionTemplate> tpl = FunctionTemplate::New(New);
  tpl->SetClassName(String::NewSymbol("SkCanvas"));
  tpl->InstanceTemplate()->SetInternalFieldCount(1);

  tpl->PrototypeTemplate()->Set(String::NewSymbol("drawColor"),
      FunctionTemplate::New(DrawColor)->GetFunction());
  tpl->PrototypeTemplate()->Set(String::NewSymbol("drawText"),
      FunctionTemplate::New(DrawText)->GetFunction());
  tpl->PrototypeTemplate()->Set(String::NewSymbol("setBitmapDevice"),
      FunctionTemplate::New(SetBitmapDevice)->GetFunction());

  constructor = Persistent<Function>::New(tpl->GetFunction());
  target->Set(String::NewSymbol("SkCanvas"), constructor);
}

Handle<Value> NodeSkiaCanvas::New(const v8::Arguments &args) {
  HandleScope scope;

  NodeSkiaCanvas* canvas = new NodeSkiaCanvas();
  canvas->Wrap(args.This());

  return args.This();
}

Handle<Value> NodeSkiaCanvas::DrawColor(const v8::Arguments &args) {
  HandleScope scope;

  NodeSkiaCanvas* canvas = ObjectWrap::Unwrap<NodeSkiaCanvas>(args.This());

  SkColor color;
  if (args[0]->IsNumber())
    color = static_cast<SkColor>(args[0]->Uint32Value());

  canvas->DrawColor(color);

  return Undefined();
}

Handle<Value> NodeSkiaCanvas::DrawText(const v8::Arguments &args) {
  HandleScope scope;

  NodeSkiaCanvas* canvas = ObjectWrap::Unwrap<NodeSkiaCanvas>(args.This());

  void *text;
  size_t byteLength;
  SkScalar x,y;
  SkPaint *skpaint;

  Local<String> text_string;
  if (args[0]->IsString())
    text_string = args[0]->ToString();
  text = reinterpret_cast<void*>(*String::Utf8Value(text_string));

  if (args[1]->IsNumber())
    byteLength = static_cast<size_t>(args[1]->Uint32Value());

  if (args[2]->IsNumber())
    x = static_cast<SkScalar>(args[2]->Uint32Value());

  if (args[3]->IsNumber())
    y = static_cast<SkScalar>(args[3]->Uint32Value());

  NodeSkiaPaint* paint = ObjectWrap::Unwrap<NodeSkiaPaint>(args[4]->ToObject());
  skpaint = paint->GetSkPaint();

  canvas->DrawText(text, byteLength, x, y, *skpaint);

  return Undefined();
}

Handle<Value> NodeSkiaCanvas::SetBitmapDevice(const Arguments &args) {
  HandleScope scope;

  NodeSkiaCanvas* canvas = ObjectWrap::Unwrap<NodeSkiaCanvas>(args.This());

  NodeSkiaBitmap* bitmap = ObjectWrap::Unwrap<NodeSkiaBitmap>(args[0]->ToObject());

  SkBitmap* skbitmap = bitmap->GetSkBitmap();

  canvas->SetBitmapDevice(*skbitmap);

  return Undefined();
}

// Wrapper functions for SkCanvas
void NodeSkiaCanvas::DrawText(const void* text, size_t byteLength,
                              SkScalar x, SkScalar y, const SkPaint& paint) {
  canvas_->drawText(text, byteLength, x, y, paint);
}

