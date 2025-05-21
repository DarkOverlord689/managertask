import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import Logo from "../assets/logo.png";
import { FiUser, FiLock, FiEye, FiEyeOff } from "react-icons/fi";
import { FcGoogle } from "react-icons/fc";
import axios from "axios";

const Login = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    role: "student",
    rememberMe: false,
  });
  const [showPassword, setShowPassword] = useState(false);
  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value,
    });

    if (errors[name]) {
      setErrors({ ...errors, [name]: "" });
    }
  };

  const validateForm = () => {
    const newErrors = {};
    if (!formData.email) newErrors.email = "Email is required";
    if (!formData.password) newErrors.password = "Password is required";

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) {
      toast.error("Please fill in all required fields");
      return;
    }

    setLoading(true);
    try {
      // Llamada directa a la API para login
      const response = await axios.post(
        `${process.env.REACT_APP_API_URL}/api/auth/login`,
        {
          email: formData.email,
          password: formData.password,
          role: formData.role,
        }
      );
      console.log("Login response:", response.data);
      //const { token, user } = response.data;
      const { access_token, user } = response.data;


      // Guardar token según "rememberMe"
      if (formData.rememberMe) {
        localStorage.setItem("authToken", access_token);
        localStorage.setItem("userRole", user.role);
      } else {
        localStorage.setItem("authToken", access_token);
        sessionStorage.setItem("userRole", user.role);
      }
      // Después de recibir la respuesta del backend
      localStorage.setItem('access_token', response.data.access_token);

      toast.success("Login successful!");

      if (user.role === "teacher") {
        navigate("/teacher-dashboard/");
      } else {
        navigate("/student-dashboard/");
      }

    } catch (error) {
      console.error("Login failed:", error);
      // Mostrar mensaje de error desde la API o genérico
      const message =
        error.response?.data?.message || "Invalid credentials. Please try again.";
      toast.error(message);
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleLogin = () => {
    // Redirigir a la ruta de login Google sin el checkToken infinito para evitar loop
    toast.info("Redirecting to Google login...");
    window.location.href = `${process.env.REACT_APP_API_URL}/api/auth/google/login`;
  };

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-white">
      <ToastContainer position="top-right" />
      <div className="h-screen w-full bg-white">
        <div className="grid grid-cols-1 md:grid-cols-2 h-full">
          {/* Left Section - Branding */}
          <div className="bg-gradient-to-br from-[#19a4db] to-[#6dc9f1] p-6 lg:p-8 xl:p-10 text-white relative overflow-hidden h-full flex flex-col justify-center">
            <h1 className="text-4xl font-bold mb-2">Bienvenido a ProFlow</h1>
            <p className="text-white/90 mb-8">
              Administra proyectos, tareas y equipos desde una sola plataforma moderna y colaborativa.
            </p>

            <div className="space-y-6 mt-8">
              <div className="flex items-center space-x-4">
                <div className="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path
                      fillRule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                      clipRule="evenodd"
                    />
                  </svg>
                </div>
                <div>
                  <h3 className="font-medium">Access Your Projects</h3>
                  <p className="text-sm text-white/70">Pick up right where you left off</p>
                </div>
              </div>

              <div className="flex items-center space-x-4">
                <div className="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9 4.804A7.968 7.968 0 005.5 4c-1.255 0-2.443.29-3.5.804v10A7.969 7.969 0 015.5 14c1.669 0 3.218.51 4.5 1.385A7.962 7.962 0 0114.5 14c1.255 0 2.443.29 3.5.804v-10A7.968 7.968 0 0014.5 4c-1.255 0-2.443.29-3.5.804V12a1 1 0 11-2 0V4.804z" />
                  </svg>
                </div>
                <div>
                  <h3 className="font-medium">Track Your Progress</h3>
                  <p className="text-sm text-white/70">See tasks, milestones, and deadlines at a glance</p>
                </div>
              </div>

              <div className="flex items-center space-x-4">
                <div className="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z" />
                    <path d="M15 7v2a4 4 0 01-4 4H9.828l-1.766 1.767c.28.149.599.233.938.233h2l3 3v-3h2a2 2 0 002-2V9a2 2 0 00-2-2h-1z" />
                  </svg>
                </div>
                <div>
                  <h3 className="font-medium">Collaborate With Your Team</h3>
                  <p className="text-sm text-white/70">Share ideas, assign tasks, and work together seamlessly</p>
                </div>
              </div>
            </div>
          </div>

          {/* Right Section - Form */}
          <div className="flex flex-col pt-16 px-4 overflow-y-auto">
            <div className="max-w-lg mx-auto w-full">
              {/* Logo */}
              <div className="flex justify-center mb-16">
                <img src={Logo} alt="VMTA" className="h-20" />
              </div>

              <h2 className="text-2xl font-bold text-gray-800 mb-1">Login to Your Account</h2>
              <p className="text-gray-600 mb-8">Enter your credentials to continue</p>

              <form onSubmit={handleSubmit} className="space-y-4">
                {/* Google Sign Up Button */}
                <button
                  type="button"
                  onClick={handleGoogleLogin}
                  className="w-full flex items-center justify-center py-3 border border-gray-300 rounded-lg text-gray-700 bg-white"
                  disabled={loading}
                >
                  <FcGoogle className="mr-2 text-xl" />
                  Sign in with Google
                </button>

                {/* Divider */}
                <div className="relative flex items-center">
                  <div className="flex-grow border-t border-gray-300"></div>
                  <span className="flex-shrink mx-4 text-gray-500 text-sm">or</span>
                  <div className="flex-grow border-t border-gray-300"></div>
                </div>

                {/* Role Selection */}
                <div className="flex justify-center mb-4 space-x-8">
                  <label className="inline-flex items-center cursor-pointer">
                    <input
                      type="radio"
                      name="role"
                      value="student"
                      checked={formData.role === "student"}
                      onChange={handleChange}
                      className="form-radio text-blue-600"
                    />
                    <span className="ml-2">Student</span>
                  </label>
                  <label className="inline-flex items-center cursor-pointer">
                    <input
                      type="radio"
                      name="role"
                      value="teacher"
                      checked={formData.role === "teacher"}
                      onChange={handleChange}
                      className="form-radio text-blue-600"
                    />
                    <span className="ml-2">Teacher</span>
                  </label>
                </div>

                {/* Email Input */}
                <div className="relative">
                  <input
                    type="email"
                    name="email"
                    placeholder="Email address"
                    value={formData.email}
                    onChange={handleChange}
                    className={`block w-full rounded-lg border px-4 py-3 pl-10 text-gray-700 placeholder-gray-400 focus:outline-none focus:ring ${
                      errors.email ? "border-red-500 focus:ring-red-400" : "border-gray-300 focus:ring-blue-500"
                    }`}
                    disabled={loading}
                  />
                  <FiUser className="absolute left-3 top-3.5 text-gray-400" />
                  {errors.email && <p className="text-red-500 text-sm mt-1">{errors.email}</p>}
                </div>

                {/* Password Input */}
                <div className="relative">
                  <input
                    type={showPassword ? "text" : "password"}
                    name="password"
                    placeholder="Password"
                    value={formData.password}
                    onChange={handleChange}
                    className={`block w-full rounded-lg border px-4 py-3 pr-10 text-gray-700 placeholder-gray-400 focus:outline-none focus:ring ${
                      errors.password ? "border-red-500 focus:ring-red-400" : "border-gray-300 focus:ring-blue-500"
                    }`}
                    disabled={loading}
                  />
                  <div
                    className="absolute right-3 top-3.5 cursor-pointer text-gray-400"
                    onClick={togglePasswordVisibility}
                  >
                    {showPassword ? <FiEyeOff /> : <FiEye />}
                  </div>
                  <FiLock className="absolute left-3 top-3.5 text-gray-400" />
                  {errors.password && <p className="text-red-500 text-sm mt-1">{errors.password}</p>}
                </div>

                {/* Remember Me */}
                <div className="flex items-center">
                  <input
                    type="checkbox"
                    name="rememberMe"
                    id="rememberMe"
                    checked={formData.rememberMe}
                    onChange={handleChange}
                    className="form-checkbox rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                    disabled={loading}
                  />
                  <label htmlFor="rememberMe" className="ml-2 block text-gray-800">
                    Remember me
                  </label>
                </div>

                {/* Submit Button */}
                <button
                  type="submit"
                  className="w-full bg-[#19a4db] hover:bg-[#1589c7] text-white rounded-lg py-3 font-semibold transition disabled:opacity-50"
                  disabled={loading}
                >
                  {loading ? "Logging in..." : "Login"}
                </button>

                <p className="mt-6 text-center text-gray-700">
                  Don't have an account?{" "}
                  <Link to="/register" className="font-semibold text-[#19a4db] hover:text-[#1589c7]">
                    Register here
                  </Link>
                </p>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
