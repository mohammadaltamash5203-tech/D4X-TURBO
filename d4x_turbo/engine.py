import sys
import os
import gc
import asyncio
import platform
import time
import socket
from concurrent.futures import ThreadPoolExecutor

class D4X_Beast_Engine:
    def __init__(self):
        self.start_time = time.time()
        self._is_optimized = False

    def boost(self):
        if self._is_optimized:
            return "⚠️ [D4X-TURBO] Engine already at Max Power!"

        try:
            # 1. Environment & Hardware Detection
            os_name = platform.system().lower()
            is_android = 'android' in os_name or 'com.termux' in sys.executable
            
            # Dynamic Thread Calculation (Jitna powerful phone/VPS, utni zyada speed)
            cpu_cores = os.cpu_count() or 2
            max_threads = min(32, cpu_cores * 4) # Server pe max 32, phone pe 16/24

            # 2. Global JSON Deep-Patching (Fastest Data Processing)
            try:
                import ujson
                sys.modules['json'] = ujson
                json_status = "ujson (Blazing Fast)"
            except ImportError:
                json_status = "standard json"

            loop = asyncio.get_event_loop()
            executor = ThreadPoolExecutor(max_workers=max_threads)
            loop.set_default_executor(executor)

            # 3. Mode Activation Logic
            if not is_android:
                # ==========================================
                # 🚀 EXTREME VPS MODE (Heavy Duty)
                # ==========================================
                try:
                    import uvloop
                    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
                    vps_status = "UVLOOP Active"
                except ImportError:
                    vps_status = "Standard Loop"
                
                # DNS optimization for ultra-fast Telegram API connection
                try:
                    import aiodns
                    dns_status = "AIODNS Active"
                except ImportError:
                    dns_status = "Standard DNS"

                # Aggressive GC for VPS (Server RAM clear rakhega)
                gc.set_threshold(1000, 50, 50)
                
                mode_status = f"🚀 ULTRA VPS MODE: {vps_status} | {dns_status}"
            
            else:
                # ==========================================
                # ⚡ TERMUX NINJA MODE (Fast but Safe)
                # ==========================================
                # Freezing Garbage Collector to prevent CPU spikes on Mobile
                gc.collect()
                gc.freeze()
                
                # Disabling asyncio debug to save Termux processing power
                if hasattr(loop, 'set_debug'):
                    loop.set_debug(False)
                
                mode_status = "⚡ TERMUX NINJA MODE: Memory Frozen & Loop Overclocked"

            self._is_optimized = True
            
            # 4. The Final Output
            boot_time = (time.time() - self.start_time) * 1000 # In milliseconds
            
            return (
                f"\n{'='*55}\n"
                f"🔥 D4X-TURBO v4.0.0 (BEAST MODE ACTIVATED) 🔥\n"
                f"{'='*55}\n"
                f"🎯 Status: {mode_status}\n"
                f"🧠 Core Workers: {max_threads} Threads Allocated\n"
                f"⚙️ Data Parser: {json_status}\n"
                f"⏱️ Boot Latency: {boot_time:.2f} ms\n"
                f"{'='*55}\n"
            )

        except Exception as e:
            return f"❌ [D4X-TURBO] System Overload Error: {str(e)}"

# Global Object
d4x = D4X_Beast_Engine()
