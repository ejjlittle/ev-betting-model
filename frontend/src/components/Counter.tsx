import { motion, useSpring, useMotionValue, useTransform } from "framer-motion";
import { formatNumber } from '@/lib/utils';
import { useEffect } from "react";

export default function Counter({ value }: {value: number}) {
    const motionValue = useMotionValue(0);
    const springValue = useSpring(motionValue, { damping: 30, stiffness: 150 });
    
    //format number dynamically
    const formattedValue = useTransform(springValue, (val) => `${formatNumber(val)}`);

    useEffect(() => {
        motionValue.set(value);
    }, [value, motionValue]);

    return (
        <motion.p>
            {formattedValue}
        </motion.p>
    );
};