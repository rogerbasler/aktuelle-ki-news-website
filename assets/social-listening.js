(() => {
  const cards = [...document.querySelectorAll('.signal-card')];
  const categoryButtons = [...document.querySelectorAll('[data-filter]')];
  const evidenceButtons = [...document.querySelectorAll('[data-evidence-filter]')];
  const status = document.querySelector('.filter-status');
  let category = 'all';
  let evidence = 'all';

  function update() {
    let visible = 0;
    cards.forEach((card) => {
      const categoryMatch = category === 'all' || card.dataset.category === category;
      const evidenceMatch = evidence === 'all' || card.dataset.evidence === evidence;
      const show = categoryMatch && evidenceMatch;
      card.classList.toggle('is-hidden', !show);
      if (show) visible += 1;
    });
    if (status) status.textContent = `${visible} von ${cards.length} Signalen sichtbar`;
  }

  categoryButtons.forEach((button) => {
    button.addEventListener('click', () => {
      category = button.dataset.filter || 'all';
      categoryButtons.forEach((item) => item.classList.toggle('is-active', item === button));
      update();
    });
  });

  evidenceButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const next = button.dataset.evidenceFilter || 'all';
      evidence = evidence === next ? 'all' : next;
      evidenceButtons.forEach((item) => item.classList.toggle('is-active', evidence !== 'all' && item === button));
      update();
    });
  });

  update();
})();
