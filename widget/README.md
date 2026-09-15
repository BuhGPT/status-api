# Виджет и бейджи BuhGPT Статус · Виджет және бейджтер

Конструктор: https://buhgpt.kz/status/ru/widget.html · https://buhgpt.kz/status/widget.html

## Карточка систем / Жүйелер карточкасы

```html
<script src="https://buhgpt.kz/status/widget.js" data-services="esf,fresh_ea,nuc,knp,kaspi,halyk" async></script>
```

## Полоса-предупреждение / Ескерту жолағы

Видна только при подтверждённом сбое или объявленных работах. Тек расталған іркіліс немесе жарияланған жұмыстар кезінде көрінеді.

```html
<script src="https://buhgpt.kz/status/widget.js" data-mode="alert" data-services="esf,fresh_ea" async></script>
```

## Параметры / Параметрлер

| Атрибут | Значения | По умолчанию |
|---|---|---|
| `data-mode` | `card`, `alert` | `card` |
| `data-services` | `id` или адреса страниц через запятую, до 12 ([SERVICES.md](../SERVICES.md)) | ключевые системы |
| `data-lang` | `auto`, `kk`, `ru` | `auto` — по браузеру посетителя, иначе `kk` |
| `data-theme` | `auto`, `light`, `dark` | `auto` |
| `data-target` | CSS-селектор элемента, куда вставить виджет | сразу после `<script>` |

Виджет рисуется в Shadow DOM — не влияет на стили сайта и не зависит от них. Данные выводятся только как текст,
ссылки ведут только на buhgpt.kz. Обновление — раз в минуту, на скрытой вкладке не обновляется.

Если на сайте строгий Content-Security-Policy, добавьте `https://buhgpt.kz` в `script-src` и `connect-src`.

## Бейджи / Бейджтер

```html
<a href="https://buhgpt.kz/status/esf/"><img src="https://buhgpt.kz/status/badge/esf.svg?lang=kk" alt="BuhGPT Статус: ЭШФ АЖ" height="20"></a>
```

```markdown
[![BuhGPT Статус: ИС ЭСФ](https://buhgpt.kz/status/badge/esf.svg?lang=ru)](https://buhgpt.kz/status/ru/esf/)
```

- `badge/{id или адрес страницы}.svg` — одна система, при сбое показывает длительность.
- `badge/all.svg` — ключевые системы: ЭСФ, СНТ, ЭЦП, КНП, 1С:Fresh, eGov, Kaspi, Halyk.
- `?lang=kk|ru` — язык; без параметра — по браузеру. Кэш — 1 минута.

Не убирайте подпись и ссылку «BuhGPT Статус». Жазу мен «BuhGPT Статус» сілтемесін алып тастамаңыз.
