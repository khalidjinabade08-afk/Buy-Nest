// import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

function App() {
  return (
    <>
    <div className="min-h-screen border flex items-center justify-center bg-[#f3f3f6]">
      <div className="w-255 h-125 rounded-3xl border border-amber-700 shadow-lg overflow-hidden bg-[#ffffff] bg-cover bg-center">
        <div className="flex p-4 items-center text-3xl font-bold text-[#111827]">
              Create new account
          <span className="ml-1 mt-2 w-2 h-2 rounded-full bg-[#2DD4BF]"></span>
        </div>

        <div className="mt-1 p-2">
          <div className="relative w-80">
            <input
              type="text"
              id="name"
              placeholder=" "
              className="peer w-80 h-13 rounded-lg border border-[#d9dedd] bg-white px-4 py-3 text-[#333333] outline-none transition-all focus:border-[#0f817a] focus:shadow-[0px_0px_4px_rgba(15,129,122,0.25)]"
            />

            <label
              htmlFor="name"
              className="absolute left-4 top-1/2 -translate-y-1/2 bg-white px-1 text-[#777777] transition-all
              peer-focus:top-0
              peer-focus:text-sm
              peer-focus:text-[#0f817a]
              peer-not-placeholder-shown:top-0`
              peer-not-placeholder-shown:text-sm"
            >
              Enter your name
            </label>
          </div>
        </div>

        <div className="mt-1 p-2">
          <div className="relative w-80">
            <input
              type="email"
              id="email"
              placeholder=" "
              className="peer w-80 h-13 rounded-lg border border-[#d9dedd] bg-white px-4 py-3 text-[#333333] outline-none transition-all focus:border-[#0f817a] focus:shadow-[0px_0px_4px_rgba(15,129,122,0.25)]"
            />
            
            <label
              htmlFor="email"
              className="absolute left-4 top-1/2 -translate-y-1/2 bg-white px-1 text-[#777777] transition-all
              peer-focus:top-0
              peer-focus:text-sm
              peer-focus:text-[#0f817a]
              peer-not-placeholder-shown:top-0`
              peer-not-placeholder-shown:text-sm"
            >
              Enter your email
            </label>
          </div>
        </div>

        <div className="mt-1 p-2">
          <div className="relative w-80">
            <input
              type="password"
              id="password"
              placeholder=" "
              className="peer w-80 h-13 rounded-lg border border-[#d9dedd] bg-white px-4 py-3 text-[#333333] outline-none transition-all focus:border-[#0f817a] focus:shadow-[0px_0px_4px_rgba(15,129,122,0.25)]"
            />

            <label
              htmlFor="password"
              className="absolute left-4 top-1/2 -translate-y-1/2 bg-white px-1 text-[#777777] transition-all
              peer-focus:top-0
              peer-focus:text-sm
              peer-focus:text-[#0f817a]
              peer-not-placeholder-shown:top-0`
              peer-not-placeholder-shown:text-sm"
            >
              Enter your password
            </label>
          </div>
        </div>

        <div className="mt-1 p-2">
          <div className="relative w-80">

            <select className="w-40 h-8 rounded-lg border border-[#d9dedd] bg-white px-4 py-1 text-[#333333] outline-none appearance-none focus:border-[#0f817a] focus:shadow-[0px_0px_4px_rgba(15,129,122,0.25)]">
              <option value="">Select you Role</option>
              <option value="customer">customer</option>
              <option value="Seller">Seller</option>
            </select>

          </div>
        </div>

        <div className="mt-1 p-2">
          <button
            type="button"
            className="w-80! cursor-pointer rounded-3xl! border border-[#0f817a] bg-[#0f817a] px-6 py-3 font-medium text-white outline-none transition-all hover:bg-[#0c6f69] focus:shadow-[0px_0px_6px_rgba(15,129,122,0.35)] active:scale-[0.98]"
          >
            Submit
          </button>
        </div>

      </div>
    </div>
    
    </>
  );
}

export default App;