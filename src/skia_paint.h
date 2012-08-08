#ifndef NODE_SKIA_PAINT_H_
#define NODE_SKIA_PAINT_H_

#include <v8.h>
#include <node.h>
#include <node_object_wrap.h>
#include <node_version.h>

#include "SkPaint.h"

class NodeSkiaPaint : public node::ObjectWrap {
public:
  static void Initialize(v8::Handle<v8::Object> target);
  static v8::Handle<v8::Value> New(const v8::Arguments &args);

  static v8::Persistent<v8::Function> constructor;

public:
  NodeSkiaPaint();
  ~NodeSkiaPaint();

private:
  SkPaint *paint_;
};



#endif
