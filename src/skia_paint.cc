#include "skia_paint.h"

#include <v8.h>
#include <node.h>
#include <node_object_wrap.h>
#include <node_version.h>

#include "SkPaint.h"

using namespace v8;
using namespace node;

Persistent<Function> NodeSkiaPaint::constructor;

NodeSkiaPaint::NodeSkiaPaint() {
}

NodeSkiaPaint::~NodeSkiaPaint() {
}

void NodeSkiaPaint::Initialize(Handle<Object> target) {
  Local<FunctionTemplate> tpl = FunctionTemplate::New(New);
  tpl->SetClassName(String::NewSymbol("SkPaint"));
  tpl->InstanceTemplate()->SetInternalFieldCount(1);

  constructor = Persistent<Function>::New(tpl->GetFunction());
  target->Set(String::NewSymbol("SkPaint"), constructor);
}

Handle<Value> NodeSkiaPaint::New(const v8::Arguments &args) {
  HandleScope scope;

  NodeSkiaPaint* paint = new NodeSkiaPaint;
  paint->Wrap(args.This());

  return args.This();
}
