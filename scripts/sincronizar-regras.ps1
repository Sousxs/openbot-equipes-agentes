<#
Distribui um arquivo de regras comuns para todos os workspaces de agentes do OpenBot
como link físico (hard link). O CLAUDE.md de cada workspace importa imported/REGRAS.md,
e o OpenBot não carrega @import de arquivo fora do workspace; o link físico resolve:
um arquivo só no disco, visível dentro de cada workspace.

Rode de novo depois de editar a fonte se o seu editor salvar gravando um arquivo novo
(salvamento "atômico" quebra o link e a fonte deixa de ser a mesma das cópias).
A fonte e os workspaces precisam estar no mesmo volume.

Uso:
  ./sincronizar-regras.ps1 -Fonte "$HOME\OpenBot\Shared\regras-comuns.md"
#>
param(
    [Parameter(Mandatory)] [string] $Fonte,
    [string] $Agents = "$HOME\OpenBot\Agents",
    [string] $Nome = 'REGRAS.md'
)
$ErrorActionPreference = 'Stop'
$Fonte = (Resolve-Path $Fonte).Path

$n = 0
foreach ($ws in Get-ChildItem $Agents -Directory -Filter 'agent-*') {
    $dir = Join-Path $ws.FullName 'imported'
    New-Item -ItemType Directory -Force $dir | Out-Null
    $alvo = Join-Path $dir $Nome
    if (Test-Path $alvo) { Remove-Item $alvo -Force }
    New-Item -ItemType HardLink -Path $alvo -Target $Fonte | Out-Null
    $n++
}
Write-Host "$n workspaces apontam para $Fonte"
