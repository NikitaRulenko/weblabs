var Like = {
  count: 0,
  doLike() {
    this.count++;
  },
  doDislike() {
    this.count--;
  }
}

Like.doLike();
Like.count;
Like.doDislike();