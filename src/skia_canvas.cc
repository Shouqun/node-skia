#include "skia_canvas.h"

#include <v8.h>
#include <node.h>
#include <node_object_wrap.h>

#include "SkCanvas.h"

using namespace v8;
using namespace node;

Persistent<Function> NodeSkiaCanvas::constructor;

NodeSkiaCanvas::NodeSkiaCanvas() {
}

NodeSkiaCanvas::~NodeSkiaCanvas() {
}

void NodeSkiaCanvas::Initialize(Handle<Object> target) {
  Local<FunctionTemplate> tpl = FunctionTemplate::New(New);
  tpl->SetClassName(String::NewSymbol("SkCanvas"));
  tpl->InstanceTemplate()->SetInternalFieldCount(1);

  constructor = Persistent<Function>::New(tpl->GetFunction());
  target->Set(String::NewSymbol("SkCanvas"), constructor);
}

Handle<Value> NodeSkiaCanvas::New(const v8::Arguments &args) {
  HandleScope scope;

  NodeSkiaCanvas* canvas = new NodeSkiaCanvas;
  canvas->Wrap(args.This());

  return args.This();
}


