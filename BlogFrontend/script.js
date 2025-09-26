const profileMenu = document.getElementById("profileMenu");
const dropdownMenu = document.getElementById("dropdownMenu");
const burger = document.getElementById("burger");
const navMenu = document.getElementById("navMenu");

// Открытие/закрытие выпадающего меню профиля
profileMenu.addEventListener("click", (e) => {
  e.stopPropagation(); // не даём клику улетать на window
  dropdownMenu.style.display =
    dropdownMenu.style.display === "block" ? "none" : "block";
});

// Клик вне меню — закрыть профильное меню
window.addEventListener("click", (e) => {
  if (!profileMenu.contains(e.target)) {
    dropdownMenu.style.display = "none";
  }
});

// Бургер-меню
burger.addEventListener("click", (e) => {
  e.stopPropagation(); // чтобы не мешал window
  navMenu.classList.toggle("active");
});

// Закрытие меню при клике на ссылку
document.querySelectorAll("#navMenu a").forEach(link => {
  link.addEventListener("click", () => {
    navMenu.classList.remove("active");
  });
});

// Кнопки
document.querySelectorAll(".like-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    btn.classList.toggle("active");
    // TODO: здесь можно отправлять запрос на сервер
  });
});

document.querySelectorAll(".dislike-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    btn.classList.toggle("active");
    // TODO: здесь можно отправлять запрос на сервер
  });
});
// Галерея: смена изображения
const mainImage = document.querySelector(".main-image img");
const thumbs = document.querySelectorAll(".thumbnails img");

thumbs.forEach(thumb => {
  thumb.addEventListener("click", () => {
    mainImage.src = thumb.src.replace("200/100", "800/400"); // берём большую версию
    thumbs.forEach(t => t.classList.remove("active"));
    thumb.classList.add("active");
  });
});
