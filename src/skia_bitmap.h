#ifndef NODE_SKIA_BITMAP_H_
#define NODE_SKIA_BITMAP_H_

#include <v8.h>
#include <node.h>
#include <node_object_wrap.h>
#include <node_version.h>

#include "SkBitmap.h"

class NodeSkiaBitmap : public node::ObjectWrap {
public:
  static void Initialize(v8::Handle<v8::Object> target);
  static v8::Handle<v8::Value> New(const v8::Arguments &args);
  static v8::Handle<v8::Value> AllocPixels(const v8::Arguments& args);
  static v8::Handle<v8::Value> SetConfig(const v8::Arguments& args);

  static v8::Persistent<v8::Function> constructor;

public:
  NodeSkiaBitmap();
  ~NodeSkiaBitmap();

  // Wrapper functions of SkBitmap
  void AllocPixels() { bitmap_->allocPixels(); };
  void SetConfig(SkBitmap::Config config, int width, int height, int rowBytes = 0) {
    bitmap_->setConfig(config, width, height, rowBytes);
  }

private:
  SkBitmap* bitmap_;
};

#endif
