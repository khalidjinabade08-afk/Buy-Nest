import "./App.css";
import image from "./images/loging-page.jpg";

function App() {
  return (
    <>
      <div className="min-h-screen flex items-center justify-center bg-[#F8F7F4] p-4">

        <div className="w-full max-w-225 h-137.5 rounded-3xl shadow-lg overflow-hidden bg-[#FFFFFF] flex">

          <div className="w-1/2 p-10">

            <div className="flex items-center text-3xl font-bold text-[#111827] mb-8">
              Create new account
              <span className="ml-1 mt-2 w-2 h-2 rounded-full bg-[#2DD4BF]"></span>
            </div>

            <div className="mt-1 p-2">
              <div className="relative w-80">
                <input
                  type="text"
                  id="name"
                  placeholder=" "
                  className="peer w-80 h-13 rounded-lg border border-[#d9dedd] bg-white px-4 py-3 text-[#333333] outline-none transition-all focus:border-[#0f817a]! focus:shadow-[0_0_0_3px_rgba(15,129,122,0.15)] "
                />

                <label
                  htmlFor="name"
                  className="absolute left-4 top-1/2 -translate-y-1/2 bg-white px-1 text-[#777777] transition-all
                  peer-focus:top-0
                  peer-focus:text-sm
                  peer-focus:text-[#0f817a]
                  peer-not-placeholder-shown:top-0
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
                  className="peer w-80 h-13 rounded-lg border border-[#d9dedd] bg-white px-4 py-3 text-[#333333] outline-none transition-all focus:border-[#0f817a]! focus:shadow-[0_0_0_3px_rgba(15,129,122,0.15)] "
                />

                <label
                  htmlFor="email"
                  className="absolute left-4 top-1/2 -translate-y-1/2 bg-white px-1 text-[#777777] transition-all
                  peer-focus:top-0
                  peer-focus:text-sm
                  peer-focus:text-[#0f817a]
                  peer-not-placeholder-shown:top-0
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
                  className="peer w-80 h-13 rounded-lg border border-[#d9dedd] bg-white px-4 py-3 text-[#333333] outline-none transition-all focus:border-[#0f817a]! focus:shadow-[0_0_0_3px_rgba(15,129,122,0.15)] "
                />

                <label
                  htmlFor="password"
                  className="absolute left-4 top-1/2 -translate-y-1/2 bg-white px-1 text-[#777777] transition-all
                  peer-focus:top-0
                  peer-focus:text-sm
                  peer-focus:text-[#0f817a]
                  peer-not-placeholder-shown:top-0
                  peer-not-placeholder-shown:text-sm"
                >
                  Enter your password
                </label>
              </div>
            </div>

            <div className="mt-1 p-2">
              <select className="w-46 h-8 rounded-lg border border-[#d9dedd] bg-white px-4 py-1 text-[#333333] outline-none focus:shadow-[0_0_0_3px_rgba(15,129,122,0.15)] ">
                <option value="">Select your Role</option>
                <option value="customer">Customer</option>
                <option value="seller">Seller</option>
              </select>
            </div>

            <div className="mt-1 p-2">
              <button
                type="button"
                className="w-80! cursor-pointer rounded-3xl! border border-[#0f817a] bg-[#0f817a] px-6 py-3 font-medium text-white hover:bg-[#0c6f69]"
              >
                Submit
              </button>
            </div>

          </div>

          <div className="relative w-1/2 h-full overflow-hidden">
            <img
              src={image}
              alt="Create account"
              className="w-full max-h-150 object-cover"
            />
            
          </div>

        </div>
      </div>
    </>
  );
}

export default App;