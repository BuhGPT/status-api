<?php
// BuhGPT Статус — открытое API. Данные: BuhGPT Статус — buhgpt.kz/status
$ctx = stream_context_create(['http' => ['timeout' => 10]]);
$json = @file_get_contents('https://buhgpt.kz/status/api/pulse/v1/context?service=esf&lang=ru', false, $ctx);
if ($json === false) {
    exit("BuhGPT Статус сейчас недоступен\n");
}
$s = json_decode($json, true);
printf("%s: %s. %s\n%s\n", $s['service_name'], $s['status_label'], $s['advice'], $s['attribution']);
