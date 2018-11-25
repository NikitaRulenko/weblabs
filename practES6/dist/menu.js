'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Menu = function () {
  function Menu(options) {
    _classCallCheck(this, Menu);

    this.options = options;
  }

  _createClass(Menu, [{
    key: 'getElem',
    value: function getElem() {
      if (!this.elem) this.render();
      return this.elem;
    }
  }, {
    key: 'render',
    value: function render() {
      var _this = this;

      this.elem = document.createElement('div');
      this.elem.className = "menu";

      var titleElem = document.createElement('span');
      this.elem.appendChild(titleElem);
      titleElem.className = "title";
      titleElem.textContent = this.options.title;

      this.elem.onmousedown = function () {
        return false;
      };

      this.elem.onclick = function (event) {
        if (event.target.closest('.title')) {
          _this.toggle();
        }
      };
    }
  }, {
    key: 'renderItems',
    value: function renderItems() {
      var items = this.options.items || [];
      var list = document.createElement('ul');
      items.forEach(function (item) {
        var li = document.createElement('li');
        li.textContent = item;
        list.appendChild(li);
      });
      this.elem.appendChild(list);
    }
  }, {
    key: 'open',
    value: function open() {
      if (!this.elem.querySelector('ul')) {
        this.renderItems();
      }
      this.elem.classList.add('open');
    }
  }, {
    key: 'close',
    value: function close() {
      this.elem.classList.remove('open');
    }
  }, {
    key: 'toggle',
    value: function toggle() {
      if (this.elem.classList.contains('open')) this.close();else this.open();
    }
  }]);

  return Menu;
}();