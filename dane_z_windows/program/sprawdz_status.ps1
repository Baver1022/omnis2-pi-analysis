# STATUS ANALIZY PI - Szczegolowy raport
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "STATUS ANALIZY PI - 10B DIGITS" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Czas sprawdzenia: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')`n"

Set-Location C:\Users\test\Analiza_10B

# [1] PROCES PYTHON
Write-Host "[1] PROCES PYTHON:" -ForegroundColor Yellow
Write-Host "----------------------------------------"
$pythonProc = Get-Process python -ErrorAction SilentlyContinue | Select-Object -Last 1
if ($pythonProc) {
    $cpuMin = [math]::Round($pythonProc.CPU/60, 1)
    $ramGB = [math]::Round($pythonProc.WorkingSet/1GB, 2)
    $runtime = (Get-Date) - $pythonProc.StartTime
    Write-Host "  PID: $($pythonProc.Id)" -ForegroundColor Green
    Write-Host "  CPU: $cpuMin minut" -ForegroundColor Green
    Write-Host "  RAM: $ramGB GB" -ForegroundColor Green
    Write-Host "  Czas dzialania: $($runtime.Hours)h $($runtime.Minutes)m" -ForegroundColor Green
    Write-Host "  Start: $($pythonProc.StartTime)" -ForegroundColor Green
} else {
    Write-Host "  [BRAK] Python nie dziala - testy zakonczone lub zatrzymane" -ForegroundColor Red
}
Write-Host ""

# [2] ZAKONCZONE TESTY
Write-Host "[2] ZAKONCZONE TESTY:" -ForegroundColor Yellow
Write-Host "----------------------------------------"
$resultFiles = Get-ChildItem *_results.json -ErrorAction SilentlyContinue | Sort-Object Name
if ($resultFiles) {
    foreach ($file in $resultFiles) {
        $json = Get-Content $file.FullName | ConvertFrom-Json
        $statusIcon = if ($json.status -eq 'completed') { '[OK]' } else { '[?]' }
        $statusColor = if ($json.status -eq 'completed') { 'Green' } else { 'Yellow' }
        Write-Host "  $statusIcon Test $($json.step_id): $($json.test_name)" -ForegroundColor $statusColor
        if ($json.execution_time) {
            $execMin = [math]::Round($json.execution_time/60, 1)
            Write-Host "       Czas: $execMin min | p-value: $($json.p_value)" -ForegroundColor Gray
        }
    }
} else {
    Write-Host "  [BRAK] Zadnych zakoczonych testow" -ForegroundColor Red
}
Write-Host ""

# [3] AKTUALNY TEST (z status.json)
Write-Host "[3] AKTUALNY TEST:" -ForegroundColor Yellow
Write-Host "----------------------------------------"
$statusFiles = Get-ChildItem *_status.json -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if ($statusFiles) {
    $status = Get-Content $statusFiles.FullName | ConvertFrom-Json
    if ($status.status -eq 'running') {
        Write-Host "  [RUNNING] Test $($status.step_id): $($status.step_name)" -ForegroundColor Cyan
        if ($status.started_at) {
            $started = [DateTime]::Parse($status.started_at)
            $elapsed = (Get-Date) - $started
            Write-Host "  Start: $($status.started_at)" -ForegroundColor Gray
            Write-Host "  Czas od startu: $($elapsed.Hours)h $($elapsed.Minutes)m" -ForegroundColor Gray
        }
    }
} else {
    Write-Host "  [BRAK] Brak informacji o aktualnym tescie" -ForegroundColor Gray
}
Write-Host ""

# [4] OSTATNIE LINIE LOGU
Write-Host "[4] OSTATNIE 5 LINII LOGU:" -ForegroundColor Yellow
Write-Host "----------------------------------------"
if (Test-Path testy_13-27_live.log) {
    Get-Content testy_13-27_live.log -Tail 5 | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }
} elseif (Test-Path full_27_live.log) {
    Get-Content full_27_live.log -Tail 5 | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }
} else {
    Write-Host "  [BRAK] Brak pliku logu" -ForegroundColor Red
}
Write-Host ""

# [5] PODSUMOWANIE
Write-Host "[5] PODSUMOWANIE:" -ForegroundColor Yellow
Write-Host "----------------------------------------"
$completed = ($resultFiles | Measure-Object).Count
$total = 27
$percent = if ($total -gt 0) { [math]::Round(100*$completed/$total, 1) } else { 0 }
Write-Host "  Zakonczone: $completed / $total testow ($percent%)" -ForegroundColor Cyan

if ($completed -gt 0 -and $pythonProc) {
    $avgTimePerTest = $pythonProc.CPU / $completed
    $remainingTests = $total - $completed
    $estimatedRemainingMin = [math]::Round($avgTimePerTest * $remainingTests / 60, 0)
    Write-Host "  Szacowany czas do konca: ~$estimatedRemainingMin minut" -ForegroundColor Cyan
}
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan

