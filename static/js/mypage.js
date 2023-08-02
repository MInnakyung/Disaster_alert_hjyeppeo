document.addEventListener("DOMContentLoaded", function () {
  // "내 위치 찾기" 텍스트 클릭 이벤트를 처리하는 함수
  function getLocation() {
    if ("geolocation" in navigator) {
      // 사용자의 허용 여부를 묻는 팝업창 띄우기
      const isAllowed = confirm("사용자의 위치 정보를 가져올까요?");
      if (isAllowed) {
        // 사용자가 허용한 경우 : 위치 정보 가져오기
        navigator.geolocation.getCurrentPosition(
          function (position) {
            // 사용자의 위치 정보를 성공적으로 가져왔을 때
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            // 위도 경도 처리
            alert("당신의 위치: 위도 " + latitude + ", 경도 " + longitude);
          },
          function (error) {
            // 위치 정보를 가져오는 중에 오류가 발생한 경우
            console.error("위치 정보 가져오기 오류:", error.message);
          }
        );
      }
    } else {
      // 브라우저가 Geolocation API를 지원하지 않는 경우
      console.error("브라우저에서 Geolocation을 지원하지 않습니다.");
    }
  }

  const getLocationText = document.getElementById("get-location");
  getLocationText.addEventListener("click", getLocation);
});