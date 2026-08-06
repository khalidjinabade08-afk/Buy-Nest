import "./App.css";

function App() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-[#181A1f]">
      <div className="w-[900px] h-[500px] rounded-2xl border border-gray-300 shadow-lg overflow-hidden bg-[#1f2329] bg-cover bg-center">

          <div className="flex p-4 items-center text-3xl font-bold text-white">
              Create new account
          <span className="ml-1 mt-2 w-2 h-2 rounded-full bg-[#2DD4BF]"></span>
          </div>

          <div className="mt-0 p-2">
            <label className="block mb-2 text-[#f5f5f5]">Name</label>
            <input type="text" placeholder="Enter your name" className="w-80 rounded-lg border border-gray-600 bg-gray-400 px-4 py-3 text-black outline-none focus:border-[#363b44]" />
          </div>

          <div className="mt-0 p-2">
            <label className="block mb-2 text-[#f5f5f5]">Email</label>
            <input type="email" placeholder="Enter your email" className="w-80 rounded-lg border border-gray-600 bg-gray-400 px-4 py-3 text-black outline-none focus:border-[#363b44]" />
          </div>

          <div className="mt-0 p-2">
            <label className="block mb-2 text-[#f5f5f5]">password</label>
            <input type="password" placeholder="Enter your password" className="w-80 rounded-lg border border-gray-600 bg-gray-400 px-4 py-3 text-black outline-none focus:border-[#363b44]" />
          </div>

          <el-dropdown class="inline-block ml-10 ">
  <button class="inline-flex w-full justify-center gap-x-1.5 rounded-md bg-white/10 px-3 py-2 text-sm font-semibold text-white inset-ring-1 inset-ring-white/5 hover:bg-white/20">
    Options
    <svg viewBox="0 0 20 20" fill="currentColor" data-slot="icon" aria-hidden="true" class="-mr-1 size-5 text-gray-400">
      <path d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z" clip-rule="evenodd" fill-rule="evenodd" />
    </svg>
  </button>

  <el-menu anchor="bottom end" popover class="w-56 origin-top-right rounded-md bg-gray-800 outline-1 -outline-offset-1 outline-white/10 transition transition-discrete [--anchor-gap:--spacing(2)] data-closed:scale-95 data-closed:transform data-closed:opacity-0 data-enter:duration-100 data-enter:ease-out data-leave:duration-75 data-leave:ease-in">
    <div class="py-1">
      <a href="#" class="block px-4 py-2 text-sm text-gray-300 focus:bg-white/5 focus:text-white focus:outline-hidden">Account settings</a>
      <a href="#" class="block px-4 py-2 text-sm text-gray-300 focus:bg-white/5 focus:text-white focus:outline-hidden">Support</a>
      <a href="#" class="block px-4 py-2 text-sm text-gray-300 focus:bg-white/5 focus:text-white focus:outline-hidden">License</a>
      <form action="#" method="POST">
        <button type="submit" class="block w-full px-4 py-2 text-left text-sm text-gray-300 focus:bg-white/5 focus:text-white focus:outline-hidden">Sign out</button>
      </form>
    </div>
  </el-menu>
</el-dropdown>

          
          
    </div>
          
    </div>
  );
}

export default App;