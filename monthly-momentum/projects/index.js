$(document).ready(function () {
  renderCurrentTime();
  renderQuote();
  renderRandomImage();
});

//현재 시간
function renderCurrentTime() {
  let url = `https://worldtimeapi.org/api/timezone/Asia/Seoul`;
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      let datetime = data["datetime"].substr(11, 5);
      // let datetime = data['datetime']
      // console.log(datetime)
      $("#currentTime").text(datetime);
    });
}

// 명언
function renderQuote() {
  let url = `https://api.quotable.io/random`;
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      let content = `" ${data["content"]} "`;
      let author = `- ${data["author"]} -`;
      $("#quoteContent").text(content);
      $("#quoteAuthor").text(author);
    });
}

// 랜덤 사진 꾸미기
function renderRandomImage() {
  let imageList = [];
  // 이미지 개수를 변경하려면 i=5의 값을 이미지 개수만큼 바꿔주세요!
  for (i = 0; i < 10; i++) {
    imageList.push(i);
  }
  let imageListLength = imageList.length;
  let randomImage = Math.floor(Math.random() * (imageListLength))+1
  randomImage = `images/${randomImage}.jpg`
  $(document.body).css("background-image", `url(${randomImage})`);
}
