#!/usr/bin/env bash
set -euo pipefail
trap 'echo "[ERROR] Falló en línea $LINENO" >&2' ERR

mkdir -p reports

# TODO: HTTP — guarda headers y explica código en 2–3 líneas al final del archivo
{
  echo "== curl -I example.com =="
  curl -Is https://example.com | sed '/^\r$/d'
  echo
  echo "Explicación : El código HTTP 200 significa que la petición fue exitosa.
Otros códigos como 301/302 indican redirecciones, y 404 significa recurso no encontrado."
} > reports/http.txt

# TODO: DNS — muestra A/AAAA/MX y comenta TTL
{
  echo "== A ==";    dig A example.com +noall +answer
  echo "== AAAA =="; dig AAAA example.com +noall +answer
  echo "== MX ==";   dig MX example.com +noall +answer
  echo
  echo "Nota: Nota : El campo TTL indica cuánto tiempo puede ser cacheada la respuesta DNS.
Un TTL alto reduce tráfico DNS pero puede retrasar cambios; un TTL bajo facilita cambios rápidos."
} > reports/dns.txt

# TODO: TLS — registra versión TLS
{
  echo "== TLS via curl -Iv =="
  curl -Iv https://example.com 2>&1 | sed -n '1,20p'
} > reports/tls.txt

# TODO: Puertos locales — lista y comenta riesgos
{
  echo "== ss -tuln =="
  ss -tuln || true
  echo
  echo "Riesgos : Puertos abiertos innecesarios exponen servicios que podrían ser explotados.
Es recomendable cerrar o filtrar los que no se usen."
} > reports/sockets.txt

echo "Reportes generados en ./reports"
