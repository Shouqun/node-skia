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
  paint_ = new SkPaint();
}

NodeSkiaPaint::~NodeSkiaPaint() {
  delete paint_;
}

void NodeSkiaPaint::Initialize(Handle<Object> target) {
  Local<FunctionTemplate> tpl = FunctionTemplate::New(New);
  tpl->SetClassName(String::NewSymbol("SkPaint"));
  tpl->InstanceTemplate()->SetInternalFieldCount(1);

  tpl->PrototypeTemplate()->Set(String::NewSymbol("setAntiAlias"),
      FunctionTemplate::New(SetAntiAlias)->GetFunction());
  tpl->PrototypeTemplate()->Set(String::NewSymbol("setTextSize"),
      FunctionTemplate::New(SetTextSize)->GetFunction());

  constructor = Persistent<Function>::New(tpl->GetFunction());
  target->Set(String::NewSymbol("SkPaint"), constructor);
}

Handle<Value> NodeSkiaPaint::New(const v8::Arguments &args) {
  HandleScope scope;

  NodeSkiaPaint* paint = new NodeSkiaPaint();
  paint->Wrap(args.This());

  return args.This();
}

Handle<Value> NodeSkiaPaint::SetAntiAlias(const v8::Arguments &args) {
  HandleScope scope;

  NodeSkiaPaint* paint = ObjectWrap::Unwrap<NodeSkiaPaint>(args.This());

  bool anti_alias = true;
  if (args[0]->IsBoolean())
    anti_alias = args[0]->BooleanValue();

  paint->SetAntiAlias(anti_alias);

  return Undefined();
}

Handle<Value> NodeSkiaPaint::SetTextSize(const v8::Arguments &args) {
  HandleScope scope;

  NodeSkiaPaint* paint = ObjectWrap::Unwrap<NodeSkiaPaint>(args.This());

  int size = 0;
  if (args[0]->IsNumber())
    size = args[0]->Uint32Value();

  paint->SetTextSize(size);

  return Undefined();
}
