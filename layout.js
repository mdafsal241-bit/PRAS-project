/* Shared sidebar layout for inner pages */
function renderLayout(activePage) {
  const nav = [
    { href: 'home.html', icon: '🏠', label: 'Dashboard' },
    { href: 'doctor.html', icon: '👨‍⚕️', label: 'Doctors' },
    { href: 'patient.html', icon: '🧑‍🦽', label: 'Patients' },
    { href: 'tablet.html', icon: '💊', label: 'Medicine Store' },
    { href: 'bmi.html', icon: '⚖️', label: 'BMI Calculator' },
    { href: 'child.html', icon: '👶', label: 'Child Health' },
    { href: 'about.html', icon: 'ℹ️', label: 'About Us' },
    { href: 'feedback.html', icon: '⭐', label: 'Reviews' },
    { href: 'contact.html', icon: '📞', label: 'Contact' },
  ];
  const links = nav.map(n =>
    `<a href="${n.href}" class="nav-item ${activePage === n.href ? 'active' : ''}"><span class="icon">${n.icon}</span> ${n.label}</a>`
  ).join('');
  return links;
}
