function showChart(imagePath, captionText) {
  const chart = document.getElementById('chart');
  const caption = document.getElementById('caption');

  chart.src = imagePath;
  chart.alt = captionText;
  caption.textContent = captionText;
}