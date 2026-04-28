// ===== Copy Prompt =====
function copyPrompt() {
  const text = document.getElementById('promptText').textContent;
  navigator.clipboard.writeText(text).then(() => {
    const btn = document.getElementById('copyBtn');
    btn.textContent = '✅ Copied!';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.textContent = '📋 Copy';
      btn.classList.remove('copied');
    }, 2000);
  }).catch(() => {
    // Fallback for older browsers
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    const btn = document.getElementById('copyBtn');
    btn.textContent = '✅ Copied!';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.textContent = '📋 Copy';
      btn.classList.remove('copied');
    }, 2000);
  });
}

// Inline copy buttons on cards
document.querySelectorAll('.copy-inline').forEach(btn => {
  btn.addEventListener('click', function(e) {
    e.preventDefault();
    const text = this.getAttribute('data-prompt');
    navigator.clipboard.writeText(text).then(() => {
      this.textContent = '✅';
      setTimeout(() => { this.textContent = 'Copy'; }, 1500);
    });
  });
});

// ===== Search =====
const searchInput = document.getElementById('searchInput');
if (searchInput) {
  searchInput.addEventListener('input', function() {
    const query = this.value.toLowerCase().trim();
    const cards = document.querySelectorAll('.prompt-card');
    const catCards = document.querySelectorAll('.category-card');
    
    if (!query) {
      cards.forEach(c => c.style.display = '');
      catCards.forEach(c => c.style.display = '');
      return;
    }
    
    cards.forEach(card => {
      const title = card.getAttribute('data-title') || '';
      const tags = card.getAttribute('data-tags') || '';
      const match = title.includes(query) || tags.includes(query);
      card.style.display = match ? '' : 'none';
    });

    // Also filter category cards if on homepage
    catCards.forEach(card => {
      const cat = card.getAttribute('data-category') || '';
      const title = (card.querySelector('h3')?.textContent || '').toLowerCase();
      const match = cat.includes(query) || title.includes(query);
      card.style.display = match ? '' : 'none';
    });
  });
}

// ===== Keyboard shortcut for search =====
document.addEventListener('keydown', function(e) {
  if (e.key === '/' && !e.ctrlKey && !e.metaKey) {
    const active = document.activeElement;
    if (active.tagName !== 'INPUT' && active.tagName !== 'TEXTAREA') {
      e.preventDefault();
      const search = document.getElementById('searchInput');
      if (search) search.focus();
    }
  }
});
