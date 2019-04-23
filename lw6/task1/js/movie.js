//d772e769273810901a6d7350592b330667838224052a74aad5470421e8663916ac099067d3fdd887fd9c0
var addMovieBlock = function (image, likes, title, info, desc, srcWatch) {
  var MoviesList = document.getElementById("movies-list");
  var MoviesListElem = document.createElement("li");
  var MoviesListImage = document.createElement("img");
  var MoviesListLikes = document.createElement("p");
  var MoviesListTitle = document.createElement("h2");
  var MoviesListInfo = document.createElement("h2");
  var MoviesListDesc = document.createElement("p");
  var MoviesListSource = document.createElement("a");

  MoviesListImage.src = image;
  MoviesListSource.href = srcWatch

  MoviesListLikes.textContent = "❤ " + likes;
  MoviesListTitle.textContent = title;
  MoviesListInfo.textContent = info;
  MoviesListDesc.textContent = desc;
  MoviesListSource.textContent = "Смотреть";

  MoviesListElem.style.listStyle = "none";
  MoviesListElem.style.height = "300px";

  MoviesListImage.style.cssFloat = "left";
  MoviesListImage.style.margin = "7px 7px 7px 0";
  MoviesListImage.style.width = "20%";
  MoviesListImage.style.height = "auto";

  MoviesListElem.appendChild(MoviesListImage);
  MoviesListElem.appendChild(MoviesListTitle);
  MoviesListElem.appendChild(MoviesListInfo);
  MoviesListElem.appendChild(MoviesListDesc);
  MoviesListElem.appendChild(MoviesListLikes);
  MoviesListElem.appendChild(MoviesListSource);

  MoviesList.appendChild(MoviesListElem);
}

var prepareUrl = function (vkAPImethod, id, count) {
  count = count || 1;
  let accessToken = "access_token=" + "d772e769273810901a6d7350592b330667838224052a74aad5470421e8663916ac099067d3fdd887fd9c0";
  return "https://api.vk.com/method/" + vkAPImethod + "?owner_id=" + id + "&count=" + count + "&" + accessToken + "&v=5.52";
};

var ajaxRequest = function (object) {
  $.ajax({
    method: object.method || "GET",
    url: object.url,

    dataType: object.type || "jsonp",
    success: object.success || function (a, b, c) {},
    error: object.error || function (a, b, c) {}
  });
};

var vkAPIResponse = function (responseData) {
  let err = responseData || 5;
  if (err === 5) {
    alert("Update vk token!");
    return;
  }
  createContent(responseData);
};

var parseResponse = function (jsonObj, condition) {
  jsonObj = jsonObj.response.items;

  var f1 = (v, s) => {
    v = v.split(s);

    for (let i = 0; i < v.length; i++) {
      if (v[i] === "" || v[i] === " " || v[i] === "\n") {
        v.splice(i, 1);
        i--;
      }
    }

    if (v[0].length > 40) v = v.splice(0, 1);
    return v;
  };

  var f2 = (v, c) => {
    v = v.split("#");

    if (v[0].indexOf("Жанр") > -1) v.splice(0, 1);

    for (let i = 0; i < v.length; i++) {
      if (v[i][0] === "#")
        v[i] = v[i].substr(1);
      else {
        v[i] = v[i].substr(0, v[i].indexOf("@"));
      }
    }

    if (c && c.constructor === Array && c.length > 0) {
      let trigLength = c.length;
      for (let i = 0; i < v.length; i++) {
        if (c.indexOf(v[i].toLowerCase()) > -1) {
          trigLength--;
        }
        if (trigLength == 0) {
          return v.join(", ");
        }
      }
    } else return v.join(", ");

    return "";
  };

  var arrRet = [];

  for (var i = 0; i < jsonObj.length; i++) {
    try {
      let tag, img, like, title, info, desc, src;
      let r = jsonObj[i];
      let obj = {
        images: "",
        likes: "",
        titles: "",
        info: "",
        descript: "",
        src: ""
      }

      if (r.text.indexOf("Страна:") > 0 && r.text.indexOf("Жанр:") > 0 && r.text.indexOf("Рейтинги:") > 0) {
        let textArr = f1(r.text, "\n");

        tag = f2(textArr[2], condition);
        if (tag == "") continue;

        img = r.attachments[0].photo.photo_807;
        if (img === "undefined" || typeof img == "undefined" || !img)
          img = r.attachments[0].photo.photo_604;

        like = r.likes.count;
        title = textArr[0].substr(0, textArr[0].indexOf("(")).trim();

        info = textArr[0].substr(textArr[0].indexOf("(")).trim();
        info += " " + textArr[1].substr(textArr[1].indexOf(":") + 1).trim();
        info += ", " + tag;

        desc = textArr[6].trim().substr(0, 185) + "...";

        src = "https://vk.com/public26750264?w=wall" + r.owner_id + "_" + r.id;

        obj.images = img;
        obj.likes = like;
        obj.titles = title;
        obj.info = info;
        obj.descript = desc;
        obj.src = src;

        arrRet.push(obj);
      }

    } catch {
      continue;
    }
  }

  return arrRet;
};

var tags = [];

function setTagSelected(e) {
  if (tags.indexOf(e.innerHTML.toLowerCase()) > -1) {
    tags.splice(tags.indexOf(e.innerHTML.toLowerCase()), 1);
    document.getElementById(e.id).style = "";
  } else {
    if (e.innerHTML.toLowerCase() !== "случайно") {
      document.getElementById("button-id-0").style = "";
      tags.push(e.innerHTML.toLowerCase());
      document.getElementById(e.id).style.backgroundColor = "#fefefe";
    } else {
      let elem = document.getElementsByClassName("button-active");
      for (let i = elem.length - 1; i > -1; i--) {
        elem[i].style = "";
      }
      tags = [];
    }
  }
  if (tags.length === 0) {
    document.getElementById("button-id-0").style.backgroundColor = "#fefefe";
  }
}

function getVKMovies(e) {
  setTagSelected(e);
  ajaxRequest({
    url: prepareUrl("wall.get", "-26750264", 100),
    method: "GET",
    success: vkAPIResponse
  });
}

var parsedContent = []
var parsedContentIt = 0;

function createContent(vkResponse) {
  var sRand = (a, b) => {
    return Math.random() - 0.5;
  };

  parsedContent = [];
  parsedContent = parseResponse(vkResponse, tags);
  parsedContent.sort(sRand);
  parsedContentIt = 0;

  reloadContent();

  if (parsedContent.length == 0) {
    addMovieBlock(
      "img/nothing.jpg",
      "",
      "Фильмов не найдено",
      "",
      "Нет фильмов соответствующим тэгам",
      ""
    );
    return;
  }

  for (let i = 0; i < parsedContent.length; i++, parsedContentIt++) {
    if (parsedContentIt === 15) break;
    addMovieBlock(
      parsedContent[i].images,
      parsedContent[i].likes,
      parsedContent[i].titles,
      parsedContent[i].info,
      parsedContent[i].descript,
      parsedContent[i].src
    );
  }

  if (parsedContent.length > 15) {
    let ButtonNext = document.createElement("button");
    ButtonNext.textContent = "Больше";
    ButtonNext.onclick = function () {
      moreMovies();
    };
    document.getElementById("button-next").appendChild(ButtonNext);
  }
}

function moreMovies() {
  let max = parsedContentIt + 15;
  if (max >= parsedContent.length) {
    document.getElementById("button-next").innerHTML = "";
  }

  for (let i = parsedContentIt; i < parsedContent.length; i++, parsedContentIt++) {
    if (parsedContentIt == max) break;
    addMovieBlock(
      parsedContent[i].images,
      parsedContent[i].likes,
      parsedContent[i].titles,
      parsedContent[i].info,
      parsedContent[i].descript,
      parsedContent[i].src
    );
  }
}

function reloadContent() {
  document.getElementById("movies-list").innerHTML = "";
  document.getElementById("button-next").innerHTML = "";
}

function buttons() {
  var ButtonsList = document.getElementById("buttons-list");
  ButtonsList.innerHTML = "";
  var ButtonsListNames = ["Случайно", "Драма", "Фэнтези", "Документальный", "Криминал",
    "Биография", "Военный", "Боевик", "Триллер", "Приключения", "Мелодрама",
    "Комедия", "Семейный", "Фантастика"
  ];
  for (let i = 0; i < ButtonsListNames.length; i++) {
    let Button = document.createElement("button");
    Button.id = "button-id-" + i;
    Button.textContent = ButtonsListNames[i];
    Button.onclick = function () {
      getVKMovies(this);
    };
    ButtonsList.appendChild(Button);
  }
}

window.onload = function () {
  buttons();
}