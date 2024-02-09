 let
   nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11";
   pkgs = import nixpkgs { config = {}; overlays = []; };
 in

 pkgs.mkShell {
   packages = with pkgs; [
     git
     neovim
     python311
     pdm
   ];

   GIT_EDITOR = "${pkgs.neovim}/bin/nvim";
   shellHook = ''
       python --version
       pdm install
       pdm build
       pdm run python -m unittest
       pdm run python hello.py -name World
   '';
 }
