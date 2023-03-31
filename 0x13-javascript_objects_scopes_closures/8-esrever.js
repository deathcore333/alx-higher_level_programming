#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while (i < len) {
    const temp = list[len];
    list[len] = list[i];
    list[i] = temp;
    i++;
    len--;
  }
  return list;
};
