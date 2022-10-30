set nohlsearch
set wildmenu
set smartindent
set shiftwidth=4
set clipboard=unnamedplus
set mouse=a
set cmdheight=1
vmap "+y :!xclip -f -sel clip
map "+p :r!xclip -o -sel clip
set nohlsearch
set wildmenu
set smartindent
set shiftwidth=4
set clipboard=unnamedplus
set mouse=a
set cmdheight=1
vmap "+y :!xclip -f -sel clip
map "+p :r!xclip -o -sel clip


inoremap ( ()<Left>
inoremap [ []<Left>
inoremap { {}<Left>

call plug#begin()
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'reconquest/vim-pythonx'
call plug#end()


" use <tab> for trigger completion and navigate to the next complete item
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction

inoremap <silent><expr> <Tab>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<Tab>" :
      \ coc#refresh()


inoremap ( ()<Left>
inoremap [ []<Left>
inoremap { {}<Left>

call plug#begin()
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'reconquest/vim-pythonx'
call plug#end()


" use <tab> for trigger completion and navigate to the next complete item
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction

inoremap <silent><expr> <Tab>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<Tab>" :
      \ coc#refresh()
