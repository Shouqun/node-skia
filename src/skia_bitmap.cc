#include "skia_bitmap.h"

#include <v8.h>
#include <node.h>
#include <node_object_wrap.h>
#include <node_version.h>

#include "SkBitmap.h"
#include "SkGraphics.h"

using namespace v8;
using namespace node;

Persistent<Function> NodeSkiaBitmap::constructor;

NodeSkiaBitmap::NodeSkiaBitmap() {
  bitmap_ = new SkBitmap();
}

NodeSkiaBitmap::~NodeSkiaBitmap() {
}

void NodeSkiaBitmap::Initialize(Handle<Object> target) {
  Local<FunctionTemplate> tpl = FunctionTemplate::New(New);
  tpl->SetClassName(String::NewSymbol("SkBitmap"));
  tpl->InstanceTemplate()->SetInternalFieldCount(1);

  // Prototype of SkBitmap
  tpl->PrototypeTemplate()->Set(String::NewSymbol("allocPixels"),
      FunctionTemplate::New(AllocPixels)->GetFunction());
  tpl->PrototypeTemplate()->Set(String::NewSymbol("setConfig"),
      FunctionTemplate::New(SetConfig)->GetFunction());

  constructor = Persistent<Function>::New(tpl->GetFunction());
  target->Set(String::NewSymbol("SkBitmap"), constructor);
}

Handle<Value> NodeSkiaBitmap::New(const v8::Arguments& args) {
  HandleScope scope;

  NodeSkiaBitmap* bitmap = new NodeSkiaBitmap();
  bitmap->Wrap(args.This());

  return args.This();
}

Handle<Value> NodeSkiaBitmap::AllocPixels(const Arguments& args) {
  HandleScope scope;

  NodeSkiaBitmap* bitmap = ObjectWrap::Unwrap<NodeSkiaBitmap>(args.This());

  bitmap->AllocPixels();

  return Undefined();
}

Handle<Value> NodeSkiaBitmap::SetConfig(const Arguments& args) {
  HandleScope scope;

  NodeSkiaBitmap* bitmap = ObjectWrap::Unwrap<NodeSkiaBitmap>(args.This());

  SkBitmap::Config config = SkBitmap::kARGB_8888_Config;
  int width = 0;
  int height = 0;

  if (args[0]->IsNumber()) {
    config = static_cast<SkBitmap::Config>(args[0]->Uint32Value());
  }

  if (args[1]->IsNumber())
    width = args[1]->Uint32Value();
  if (args[2]->IsNumber())
    height = args[2]->Uint32Value();

  bitmap->SetConfig(config, width, height);

  return Undefined();
}
