function copyToClipboard() {
  /* Получить текстовое поле */
  var copyText = document.getElementsByName("translation")[0];

  /* Выделите текстовое поле */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* Для мобильных устройств */

  /* Скопируйте текст внутри текстового поля */
  document.execCommand("copy");
}