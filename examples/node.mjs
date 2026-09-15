// Node.js 18+ (встроенный fetch). Данные: BuhGPT Статус — buhgpt.kz/status
const BASE = "https://buhgpt.kz/status/api/pulse/v1";

const summary = await (await fetch(`${BASE}/summary?lang=ru`)).json();
const problems = summary.groups
  .flatMap((g) => g.services)
  .filter((s) => !["OPERATIONAL", "UNKNOWN"].includes(s.status));

if (problems.length === 0) {
  console.log(`Все системы работают. ${summary.provider.attribution}`);
} else {
  for (const s of problems) {
    const ctx = await (await fetch(`${BASE}/context?service=${s.id}&lang=ru`)).json();
    console.log(`${ctx.service_name}: ${ctx.status_label}. ${ctx.advice}`);
  }
  console.log(summary.provider.attribution);
}
